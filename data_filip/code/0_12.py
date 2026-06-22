def extract_digits(s):
    result = []
    for char in s:
        if char >= '0' and char <= '9':
            result.append(char)
    return result

if __name__ == '__main__':
    sample_string = "a1b2c3d4e5f6g7h8i9j0!@#$%^&*()"
    print(extract_digits(sample_string))