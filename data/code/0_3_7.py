def extract_digits(text):
    return ''.join(ch for ch in text if ch.isdigit())

if __name__ == '__main__':
    result = extract_digits("a1b2c3")
    print(result)