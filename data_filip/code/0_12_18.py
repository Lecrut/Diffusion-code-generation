def extract_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample = "a1b2!c3 d4#e5"
    print(extract_digits(sample))