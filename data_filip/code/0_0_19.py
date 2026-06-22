def extract_digits(text):
    digits = "".join(c for c in text if c.isdigit())
    if not digits:
        return 0
    return int(digits)

if __name__ == '__main__':
    result = extract_digits("a1b2c3d4")
    print(result)
    
    result_empty = extract_digits("abc")
    print(result_empty)
    
    result_mixed = extract_digits("123")
    print(result_mixed)