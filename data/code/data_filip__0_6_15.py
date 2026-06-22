def extract_digits_count(s):
    return sum(1 for c in s if c.isdigit())

if __name__ == '__main__':
    print(extract_digits_count("a1b2c3"))
    print(extract_digits_count("hello"))
    print(extract_digits_count("12345"))
    print(extract_digits_count("test123abc456"))