import string

def count_special_characters(s):
    special_chars = set(string.punctuation)
    count = 0
    for char in s:
        if char in special_chars:
            count += 1
    return count, count > 0

if __name__ == '__main__':
    sample_string = "Hello, World! How are you?"
    result = count_special_characters(sample_string)
    print(result)