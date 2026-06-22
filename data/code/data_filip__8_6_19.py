import re

def split_and_strip(input_string):
    return [part.strip() for part in input_string.split(',') if part.strip()]

if __name__ == '__main__':
    result = split_and_strip(" hello , world , , foo , bar ")
    print(result)