def extract_digits(s):
    return ''.join(ch for ch in s if ch.isdigit())

if __name__ == '__main__':
    text = "a1b2c3d4e5"
    result = extract_digits(text)
    print(result)