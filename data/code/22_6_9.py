def validate_password(password: str) -> bool:
    if not password:
        return False
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        else:
            return False
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    max_consecutive = 0
    current_consecutive = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
        else:
            current_consecutive = 1
    if max_consecutive > 3:
        return False
    return True
if __name__ == '__main__':
    test_passwords = ['Aa1!Bb2@', 'aaaa1111!', 'Aa1!', 'Aa1!bbbb', 'Short1!', 'NoSpecial1a', 'Aa1!bbbb2']
    for pw in test_passwords:
        result = validate_password(pw)
        print(f'{pw}: {result}')