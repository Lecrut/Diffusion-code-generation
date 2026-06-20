def extract_digits(text):
    return [char for char in text if char.isdigit()]

if __name__ == '__main__':
    sample1 = "abc123def456ghi"
    sample2 = "Hello World! 123 @#$ 456"
    sample3 = ""
    sample4 = "no digits here"
    sample5 = "9a8b7c6d5e4f3g2h1i0j"

    print(extract_digits(sample1))
    print(extract_digits(sample2))
    print(extract_digits(sample3))
    print(extract_digits(sample4))
    print(extract_digits(sample5))