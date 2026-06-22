def is_valid_phone_number(phone: str) -> bool:
    if not phone:
        return False
    if phone[0] != '+':
        return False
    rest = phone[1:]
    if not rest.isdigit():
        return False
    for i in range(1, 4):
        country_code = rest[:i]
        subscriber_number = rest[i:]
        if len(country_code) != i:
            continue
        if len(subscriber_number) < 7 or len(subscriber_number) > 10:
            continue
        return True
    return False
if __name__ == '__main__':
    print(is_valid_phone_number('+12345678901'))
    print(is_valid_phone_number('+14567890123'))
    print(is_valid_phone_number('+45678901'))
    print(is_valid_phone_number('+123456789012'))
    print(is_valid_phone_number('12345678901'))
    print(is_valid_phone_number('+1234567'))
    print(is_valid_phone_number('+'))
    print(is_valid_phone_number(''))