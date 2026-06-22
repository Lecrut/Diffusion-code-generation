def is_valid_phone_number(phone: str) -> bool:
    if not phone:
        return False
    if phone[0] != '+':
        return False
    rest = phone[1:]
    digits_only = rest.isdigit()
    if not digits_only:
        return False
    length = len(rest)
    if length < 8 or length > 13:
        return False
    for cc_len in range(1, 4):
        if len(rest) - cc_len < 7 or len(rest) - cc_len > 10:
            continue
        return True
    return False
if __name__ == '__main__':
    test_cases = [('+1234567890', True), ('+14567890', True), ('+123456789', True), ('+12345678', True), ('+1234567', True), ('+123456', False), ('+12345', False), ('+1234', False), ('+123', False), ('+12', False), ('+1', False), ('1234567890', False), ('+12345678901', True), ('+123456789012', True), ('+1234567890123', True), ('+12345678901234', False), ('+123456789012345', False), ('', False), ('+', False), ('+abc', False), ('+12abc', False), ('+1234567890x', False)]
    for phone, expected in test_cases:
        result = is_valid_phone_number(phone)
        print(result)