def extract_digits(text):
    return [ch for ch in text if ch.isdigit()]

if __name__ == '__main__':
    sample_text = "abc123!@# 456 def789"
    result = extract_digits(sample_text)
    print(result)