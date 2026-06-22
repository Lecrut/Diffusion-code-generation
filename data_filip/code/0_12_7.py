def extract_digits(text):
    return [ch for ch in text if ch.isdigit()]

if __name__ == '__main__':
    sample = "a1b2!3@4#5c6d7 e8f9g0"
    result = extract_digits(sample)
    print(result)