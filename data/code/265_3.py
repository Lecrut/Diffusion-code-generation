def extract_digits(input_string):
    digits = []
    for char in input_string:
        if char.isdigit():
            digits.append(int(char))
    return digits
if __name__ == '__main__':
    test_string1 = "abc123xyz45"
    result1 = extract_digits(test_string1)
    print(result1)
    test_string2 = "No digits here"
    result2 = extract_digits(test_string2)
    print(result2)
    test_string3 = "98765"
    result3 = extract_digits(test_string3)
    print(result3)