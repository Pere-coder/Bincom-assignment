import requests
from bs4 import BeautifulSoup
import lxml


#inother for me to get the data from the html page, i scraped the data using beautiful soup

url = "http://127.0.0.1:5500/bincom.html"
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')
scraped_data = soup.find_all('tr')
data_list = []
for data in scraped_data:
    data = data.find_all('td')
    if len(data) >= 2:
        final_data = data[1].get_text()
        data_list.append(final_data)

new_list = []
for color in data_list:
    c = color.lower().strip()
    data = c.split(',')
    for i in data:
        new_list.append(i)

#i stored all the colours in a list called new_list


# Which color of shirt is the mean color?

color_counts = {}

for color in new_list:
    color = color.strip().lower()
    if color in color_counts:
        color_counts[color] +=1
    else:
        color_counts[color] = 1
mean_color = max(color_counts, key=color_counts.get)

print(f'{mean_color} is the mean color ')
#The color worn throughout the week is also the mean color
print(f'{mean_color} is also the color worn throughout the week')




# Which color is the median?
sorted_data = sorted(new_list)
num_colors = len(sorted_data)
median_index = num_colors//2
print(median_index)
if num_colors % 2 ==1:
    median_color = sorted_data[median_index]
else:
    median_color = sorted_data[median_index - 1]
print(f'the median color is {median_color}')




#colors and frequency
import psycopg2
from collections import Counter


color_occurance = Counter(new_list)

#I Established a connection to my PostgreSQL database
conn = psycopg2.connect(
    host="127.0.0.1",
    database="Bincom",
    user="postgres",
    password="postgres"
)
#i created a cursor ovject to execute SQL statements
cursor = conn.cursor()

# Iterate through the color_counts dictionary and insert data into the table
for color, frequency in color_occurance.items():
    sql = "INSERT INTO color_frequency (color, frequency) VALUES (%s, %s)"
    cursor.execute(sql, (color, frequency))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random

random_digit = random.randint(0, 15)
binary = bin(random_digit)[2:].zfill(4)
base_10 = random_digit
print(f'binary : {binary}, base 10:{base_10}')



# Write a program to sum the first 50 fibonacci sequence
def fibonacci_sum(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return sum(fib_sequence)


fib_sum = fibonacci_sum(50)
print("Sum of the first 50 Fibonacci numbers:", fib_sum)
