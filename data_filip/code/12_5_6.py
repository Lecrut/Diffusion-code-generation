def check_phone_number(phone):
    if not isinstance(phone, str) or len(phone) == 0:
        return False
    if phone[0] != '+':
        return False
    digits_part = phone[1:]
    if not digits_part.isdigit():
        return False
    digit_count = len(digits_part)
    if digit_count < 8 or digit_count > 13:
        return False
    parts = phone[1:]
    country_code_end = 0
    for i in range(1, 4):
        if i <= digit_count:
            country_code_end = i
            break
    remaining_digits = digit_count - country_code_end
    if remaining_digits < 7 or remaining_digits > 10:
        return False
    return True

if __name__ == '__main__':
    print(check_phone_number('+1234567890'))
    print(check_phone_number('+12345678'))
    print(check_phone_number('+123456'))
    print(check_phone_number('+1234567890123'))
    print(check_phone_number('1234567890'))
    print(check_phone_number('+abc123456'))
    print(check_phone_number('+'))
    print(check_phone_number('+12'))
    print(check_phone_number('+1234567'))
    print(check_phone_number('+123456789'))