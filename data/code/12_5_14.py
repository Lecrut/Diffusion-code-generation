def check_phone_number(phone):
    if not phone or phone[0] != '+':
        return False
    
    digits = phone[1:]
    
    if not digits.isdigit():
        return False
    
    length = len(digits)
    return 8 <= length <= 13

if __name__ == '__main__':
    print(check_phone_number('+1234567890'))
    print(check_phone_number('+1234567'))
    print(check_phone_number('+1234567890123'))
    print(check_phone_number('1234567890'))
    print(check_phone_number('+123456'))