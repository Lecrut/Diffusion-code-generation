def check_password_strength(password: str) -> bool:
    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_special = 0
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper |= 1
        if 97 <= code <= 122:
            has_lower |= 2
        if 48 <= code <= 57:
            has_digit |= 4
        if 33 <= code <= 47 or 58 <= code <= 64 or 91 <= code <= 96 or (123 <= code <= 126):
            has_special |= 8
    return has_upper | has_lower | has_digit | has_special == 15

def evaluate_password(password: str) -> str:
    if check_password_strength(password):
        return 'Strong'
    else:
        return 'Weak'
if __name__ == '__main__':
    test_passwords = ['Hello1!', 'weak', 'ALLCAPS123!', 'noNumbersAndNoSpecial', 'MixedCase123@#']
    results = []
    for pwd in test_passwords:
        strength = evaluate_password(pwd)
        results.append(f'{pwd}: {strength}')
    output = '\n'.join(results)
    print(output)