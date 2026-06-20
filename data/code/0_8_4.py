def extract_and_sum_digits(s: str) -> int:
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample1 = "a1b2c3"
    print(extract_and_sum_digits(sample1))
    sample2 = "no_digits_here"
    print(extract_and_sum_digits(sample2))
    sample3 = "007_james_bond"
    print(extract_and_sum_digits(sample3))
    sample4 = ""
    print(extract_and_sum_digits(sample4))
    sample5 = "12345"
    print(extract_and_sum_digits(sample5))