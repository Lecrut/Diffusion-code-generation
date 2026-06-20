mixed_string = "abc123def456ghi789"

def extract_digits(s):
    return "".join(c for c in s if c.isdigit())

if __name__ == '__main__':
    result = extract_digits(mixed_string)
    print(result)