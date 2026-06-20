def extract_digits(text):
    return ''.join(ch for ch in text if ch.isdigit())

if __name__ == '__main__':
    mixed_string = "abc123def456"
    result = extract_digits(mixed_string)
    print(result)