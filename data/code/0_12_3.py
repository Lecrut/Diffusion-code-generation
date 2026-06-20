def extract_digits(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample = "a1b2c3!@# d4e5f6 7g8h9i0"
    print(extract_digits(sample))