import string

def count_special_chars(s):
    special_characters = set(string.punctuation)
    count = 0
    for char in s:
        if char in special_characters:
            count += 1
    return count, count > 0

if __name__ == '__main__':
    sample_string = "Hello, World! @Python#2023"
    result = count_special_chars(sample_string)
    print(result)