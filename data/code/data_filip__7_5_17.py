import string

def count_special_chars(text):
    special_chars = set(string.punctuation)
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello, world!"
    count_result = count_special_chars(sample_text)
    has_special = count_result > 0
    print(count_result)
    print(has_special)