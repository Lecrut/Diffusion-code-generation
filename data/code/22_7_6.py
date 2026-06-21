def check_password_strength(password):
    mask = 0
    for char in password:
        code = ord(char)
        if 48 <= code <= 57:
            mask |= 1
        elif 65 <= code <= 90:
            mask |= 2
        elif 97 <= code <= 122:
            mask |= 4
        elif 33 <= code <= 47 or 58 <= code <= 64 or 91 <= code <= 96 or 123 <= code <= 126:
            mask |= 8
    return mask

if __name__ == '__main__':
    result = check_password_strength("MyP@ssw0rd!")
    print(result)