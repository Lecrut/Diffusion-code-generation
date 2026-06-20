def extract_digits(s):
    return "".join(c for c in s if c.isdigit())

if __name__ == '__main__':
    mixed_string = "Project99: alpha-2024-beta3"
    result = extract_digits(mixed_string)
    print(result)