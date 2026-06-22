def extract_digits(text):
    return "".join(c for c in text if c.isdigit())

if __name__ == '__main__':
    mixed_string = "abc123def456ghi789"
    result = extract_digits(mixed_string)
    print(result)