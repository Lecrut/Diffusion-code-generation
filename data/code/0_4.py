def sanitize_to_float(text):
    digits = [char for char in text if char.isdigit() or char == '.']
    cleaned = ''.join(digits)
    if not cleaned or cleaned == '.':
        return 0.0
    return float(cleaned)

if __name__ == '__main__':
    sample1 = "Price: $123.45 for 2 items!"
    sample2 = "Error code: ABC-999-xyz"
    sample3 = "No numbers here!!"
    sample4 = "Mixed: 10.5 and 20.5 and 30.5"
    print(sanitize_to_float(sample1))
    print(sanitize_to_float(sample2))
    print(sanitize_to_float(sample3))
    print(sanitize_to_float(sample4))