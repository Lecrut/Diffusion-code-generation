def is_valid_phone_number(phone: str) -> bool:
    if not phone:
        return False
    if not phone.startswith('+'):
        return False
    rest = phone[1:]
    if not rest:
        return False
    if not rest[0].isdigit():
        return False
    digit_count = 0
    for char in rest:
        if char.isdigit():
            digit_count += 1
        else:
            return False
    if 1 <= digit_count <= 13:
        country_digits = 0
        for char in rest:
            if char.isdigit():
                country_digits += 1
            else:
                break
        if 1 <= country_digits <= 3:
            remaining_digits = digit_count - country_digits
            if 7 <= remaining_digits <= 10:
                return True
    return False

if __name__ == '__main__':
    print(is_valid_phone_number("+1234567890"))
    print(is_valid_phone_number("+1456789"))
    print(is_valid_phone_number("+441234567890"))
    print(is_valid_phone_number("+1234567"))
    print(is_valid_phone_number("1234567890"))
    print(is_valid_phone_number("+12345678901"))