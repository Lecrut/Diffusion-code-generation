def sanitize_to_float(text):
    digits = ''.join(char for char in text if char.isdigit())
    if digits == '':
        return 0.0
    return float(digits)

if __name__ == '__main__':
    print(sanitize_to_float("abc123.45xyz!@#678"))
    print(sanitize_to_float("no digits here!"))
    print(sanitize_to_float("99.99"))