def check_phone_number(phone: str) -> bool:
    if not phone:
        return False
    if not phone.startswith('+'):
        return False
    rest = phone[1:]
    if not rest.isdigit():
        return False
    total_len = len(rest)
    if total_len < 8 or total_len > 13:
        return False
    area_code = rest[:3]
    if area_code[0] == '0':
        return False
    return True

if __name__ == '__main__':
    test_numbers = [
        "+1234567890",
        "+123456789",
        "+12345678",
        "+1234567",
        "+0123456789",
        "1234567890",
        "+12345678901234",
        "+12345678901",
        "+123456789012"
    ]
    for num in test_numbers:
        result = check_phone_number(num)
        print(f"{num}: {result}")