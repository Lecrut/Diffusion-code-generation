def strip_and_check_phone_number(phone_number):
    digits = ''.join(c for c in phone_number if c.isdigit())
    return digits, len(digits) == 11

if __name__ == '__main__':
    sample1 = "123-456-7890"
    result1 = strip_and_check_phone_number(sample1)
    print(result1)
    sample2 = "12345678901"
    result2 = strip_and_check_phone_number(sample2)
    print(result2)
    sample3 = "+1 (234) 567-8901"
    result3 = strip_and_check_phone_number(sample3)
    print(result3)