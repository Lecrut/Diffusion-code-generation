def extract_digits(text: str) -> list:
    result = []
    for char in text:
        if '0' <= char <= '9':
            result.append(char)
    return result

if __name__ == '__main__':
    sample_string = "abc123!@#456 def 789"
    digits = extract_digits(sample_string)
    print(digits)