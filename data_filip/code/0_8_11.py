def extract_and_sum_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample1 = "a1b2c3"
    sample2 = "no digits here"
    sample3 = "123abc456def789"
    print(extract_and_sum_digits(sample1))
    print(extract_and_sum_digits(sample2))
    print(extract_and_sum_digits(sample3))