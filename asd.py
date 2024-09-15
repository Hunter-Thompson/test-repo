## create a script that will create a bunch of files with random titles replacing space with underscore and random content 

import os
import random

def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

def random_content(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for i in range(length))

def create_file():
    title = random_string(10)
    title2 = random_string(10)
    content = random_content(100)
    with open(f'{title}_{title2}.md', 'w') as file:
        file.write(content)

def main():
    for i in range(10):
        create_file()

if __name__ == '__main__':
    main()
