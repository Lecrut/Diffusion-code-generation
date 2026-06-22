def extract_digits(s: str) -> str:
    result = []
    for char in s:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "a1b2c3D4e5F6g7H8i9J0!@#kLmN"
    extracted = extract_digits(sample_string)
    print(extracted)