import string

def count_special_characters(text):
    special_chars = set(string.punctuation)
    count = 0
    has_special = False
    for char in text:
        if char in special_chars:
            count += 1
            has_special = True
    return count, has_special

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_special_characters(sample_text)
    print(result)