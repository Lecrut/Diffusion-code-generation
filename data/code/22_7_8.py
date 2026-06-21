def check_password(password):
    if not password:
        return 0
    flags = 0
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            flags |= 1
        elif 97 <= code <= 122:
            flags |= 2
        elif 48 <= code <= 57:
            flags |= 4
        elif not (65 <= code <= 90 or 97 <= code <= 122 or 48 <= code <= 57):
            flags |= 8
    return flags

if __name__ == '__main__':
    sample_password = "P@ssw0rd"
    result = check_password(sample_password)
    print(result)