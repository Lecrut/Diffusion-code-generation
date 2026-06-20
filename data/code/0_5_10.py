def extract_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(int(char))
    return result

if __name__ == '__main__':
    text = "a1b2c3"
    digits = extract_digits(text)
    print(digits)