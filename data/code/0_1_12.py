def extract_numeric_string(s):
    numeric_chars = [char for char in s if char.isdigit()]
    return "".join(numeric_chars)

if __name__ == '__main__':
    sample_string = "abc123xyz456!@#789"
    result = extract_numeric_string(sample_string)
    print(result)