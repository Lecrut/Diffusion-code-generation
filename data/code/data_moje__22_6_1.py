def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
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
    sample_passwords = ["Abc12345!", "AAAA1234!", "A1234567!", "abc123", "ValidPass1!"]
    results = {}
    for pwd in sample_passwords:
        results[pwd] = is_valid_password(pwd)
    print(results)