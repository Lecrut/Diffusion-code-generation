def is_valid_phone_number(phone_number: str) -> bool:
    if not phone_number:
        return False
    if not phone_number.startswith('+'):
        return False
    rest = phone_number[1:]
    if not rest:
        return False
    if not rest[0].isdigit():
        return False
    if not rest[-1].isdigit():
        return False
    index = 0
    while index < len(rest) and rest[index].isdigit():
        index += 1
    leading_digits = index
    if leading_digits < 1 or leading_digits > 3:
        return False
    remaining = rest[index:]
    if not remaining:
        return False
    if not all(c.isdigit() for c in remaining):
        return False
    if len(remaining) < 7 or len(remaining) > 10:
        return False
    return True

if __name__ == '__main__':
    sample_numbers = ["+11234567890", "+4420712345678", "+9876543210", "+1234567", "+9123456789", "+123456789012", "1234567890", "+", "+1234567890"]
    for number in sample_numbers:
        print(is_valid_phone_number(number))