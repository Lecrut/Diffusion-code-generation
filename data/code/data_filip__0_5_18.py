def extract_digits(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    digits = []
    for char in text:
        if char.isdigit():
            digits.append(int(char))
    
    return digits

if __name__ == '__main__':
    sample_text = "abc123xy4!@#56"
    result = extract_digits(sample_text)
    print(result)