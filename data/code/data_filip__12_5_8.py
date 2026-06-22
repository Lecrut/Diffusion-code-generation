def is_valid_phone_number(phone_number: str) -> bool:
    if not isinstance(phone_number, str):
        return False
    if not phone_number.startswith('+'):
        return False
    remainder = phone_number[1:]
    if not remainder.isdigit():
        return False
    length = len(remainder)
    total_length = length + 1
    if 8 <= total_length <= 14:
        return True
    if 8 <= length <= 11:
        first_part = remainder[:3]
        second_part = remainder[3:]
        if second_part.isdigit():
            second_length = len(second_part)
            if 7 <= second_length <= 10:
                return True
        return False
    return False

if __name__ == '__main__':
    samples = [
        '+11234567890',
        '+12345678',
        '+1234567',
        '+12345678901',
        '+123456789',
        '123456789',
        '+123456789012',
        '+123456',
        '+',
        '+12'
    ]
    for s in samples:
        print(is_valid_phone_number(s))