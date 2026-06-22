def check_phone_number(phone_number):
    if not phone_number:
        return False
    if phone_number[0] != '+':
        return False
    rest = phone_number[1:]
    if not rest.isdigit():
        return False
    if len(rest) < 8 or len(rest) > 13:
        return False
    prefix_length = 0
    for char in rest:
        if char.isdigit():
            prefix_length += 1
        else:
            break
    if prefix_length < 1 or prefix_length > 3:
        return False
    total_digits = sum(1 for c in rest if c.isdigit())
    if total_digits < 8 or total_digits > 13:
        return False
    remaining_digits = total_digits - prefix_length
    if remaining_digits < 7 or remaining_digits > 10:
        return False
    return True

if __name__ == '__main__':
    samples = [
        "+1234567890",
        "+123456789",
        "+12345678901",
        "+1234567",
        "+12345",
        "1234567890",
        "+abc1234567",
        "+12345678",
        "+12345678901234",
        "+1234567890123",
        "+123456789012",
        "",
        "+",
        "+1",
        "+12",
        "+123",
        "+1234",
    ]
    for sample in samples:
        print(check_phone_number(sample))