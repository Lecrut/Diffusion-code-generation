import re

def count_consonants(text):
    vowels = "aeiouAEIOU"
    letter_pattern = re.compile(r"[a-zA-Z]")
    count = 0
    for char in text:
        if letter_pattern.match(char) and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    test_string = "Hello World! 123 AEIOU bdfg"
    result = count_consonants(test_string)
    print(result)