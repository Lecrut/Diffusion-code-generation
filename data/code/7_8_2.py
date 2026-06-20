import string

def count_special_chars(text):
    special_chars = set(string.punctuation) + set(' \t\n\r')
    count = 0
    status = False
    for char in text:
        if char in special_chars:
            count += 1
            status = True
    return count, status

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_special_chars(sample_text)
    print(result)