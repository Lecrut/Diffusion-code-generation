def extract_digits_from_string(text):
    result = []
    for char in text:
        if '0' <= char <= '9':
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    mixed_string = "abc123def456ghi789"
    digits_str = extract_digits_from_string(mixed_string)
    result = int(digits_str) if digits_str else 0
    print(result)