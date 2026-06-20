def extract_and_sum_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample1 = "a1b2c3"
    print(extract_and_sum_digits(sample1))
    sample2 = "no digits here"
    print(extract_and_sum_digits(sample2))
    sample3 = "999"
    print(extract_and_sum_digits(sample3))
    sample4 = "abc123xyz789"
    print(extract_and_sum_digits(sample4))
    sample5 = ""
    print(extract_and_sum_digits(sample5))