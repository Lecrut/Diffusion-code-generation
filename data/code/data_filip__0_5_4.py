def extract_digits(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(int(char))
    return result

if __name__ == '__main__':
    sample = "abc123def456ghi789"
    digits = extract_digits(sample)
    print(digits)