def extract_digits(text):
    digits = []
    for char in text:
        if char.isdigit():
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample = "a1b2c3"
    print(extract_digits(sample))