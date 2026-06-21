import re

def find_all_letters(text):
    letters = set()
    for char in text:
        if char.isalpha():
            letters.add(char.lower())
    return letters

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with mixed cases and numbers 123."
    result = find_all_letters(sample_string)
    print(result)