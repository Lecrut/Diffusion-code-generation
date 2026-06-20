def extract_digits(s: str) -> str:
    return ''.join(c for c in s if c.isdigit())

if __name__ == '__main__':
    sample1 = "Hello, World! 123 456 @#$ abc"
    sample2 = "No digits here!"
    sample3 = "0a1b2c3d4e5f"
    print(extract_digits(sample1))
    print(extract_digits(sample2))
    print(extract_digits(sample3))