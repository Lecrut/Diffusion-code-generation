import string

def count_special_characters(text):
    special_chars = set(string.punctuation)
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count > 0

if __name__ == '__main__':
    sample_text = "Hello, World! #Python3"
    result = count_special_characters(sample_text)
    print(result)