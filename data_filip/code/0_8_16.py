def extract_and_sum_digits(s):
    digits = []
    for char in s:
        if char.isdigit():
            digits.append(int(char))
    return sum(digits)

if __name__ == '__main__':
    print(extract_and_sum_digits("abc123def45"))
    print(extract_and_sum_digits("no digits here"))
    print(extract_and_sum_digits("9a8b7"))
    print(extract_and_sum_digits(""))
    print(extract_and_sum_digits("000"))
    print(extract_and_sum_digits("123abc456def789"))