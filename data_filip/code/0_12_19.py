def extract_digits(text):
    result = []
    for char in text:
        if '0' <= char <= '9':
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "abc123!@# 456 xyz 789"
    digits = extract_digits(sample_text)
    print(digits)