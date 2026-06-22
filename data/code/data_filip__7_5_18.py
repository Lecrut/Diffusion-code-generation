import string

def count_special_characters(text):
    special_chars = set(string.punctuation)
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count

if __name__ == '__main__':
    text_sample = "Hello, World! 123"
    count = count_special_characters(text_sample)
    print(count > 0)