def strip_non_digits_and_check(phone_number: str) -> bool:
    digits = ''.join(c for c in phone_number if c.isdigit())
    return len(digits) == 11

if __name__ == '__main__':
    sample1 = "+1 (555) 123-4567"
    sample2 = "55512345678"
    sample3 = "123"
    print(strip_non_digits_and_check(sample1))
    print(strip_non_digits_and_check(sample2))
    print(strip_non_digits_and_check(sample3))