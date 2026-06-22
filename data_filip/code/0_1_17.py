def extract_numeric_string(text):
    return ''.join([char for char in text if char.isdigit()])

if __name__ == '__main__':
    sample_text = "abc123def456ghi789jkl012"
    result = extract_numeric_string(sample_text)
    print(result)