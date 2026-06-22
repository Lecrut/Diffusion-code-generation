import string
import pandas as pd

def contains_special_characters(s):
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in s)

if __name__ == '__main__':
    print(contains_special_characters("Hello World"))
    print(contains_special_characters("Hello, World!"))
    print(contains_special_characters("Python3.9"))
    print(contains_special_characters(""))
    print(contains_special_characters("@#$%"))