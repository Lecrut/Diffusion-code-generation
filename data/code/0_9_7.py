def extract_digits(text):
    return "".join(char for char in text if char.isdigit())

if __name__ == '__main__':
    mixed_string = "a1b2c3d4e5"
    result = extract_digits(mixed_string)
    print(result)