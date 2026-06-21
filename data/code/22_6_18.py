def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(not c.isalnum() for c in password):
        return False
    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count > 3:
                return False
        else:
            count = 1
    return True

if __name__ == '__main__':
    sample_passwords = [
        "Abc123!@#",
        "aaaaB1!@#",
        "Abc123",
        "Abcdefg1!",
        "ABCD1234!",
        "Ab1!Ab1!",
        "Aaaa123!b"
    ]
    results = [validate_password(p) for p in sample_passwords]
    print(results)