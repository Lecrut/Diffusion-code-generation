def extract_digits(text):
    return ''.join(c for c in text if c.isdigit())

if __name__ == '__main__':
    sample_text = "abc123def45ghi678jkl"
    result = extract_digits(sample_text)
    print(result)