def extract_digits(s):
    return ''.join(ch for ch in s if ch.isdigit())

if __name__ == '__main__':
    mixed_string = "abc123def456ghi789"
    result = extract_digits(mixed_string)
    print(result)