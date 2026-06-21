COMMON_COMPROMISED_PASSWORDS = frozenset([
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "monkey",
    "1234567",
    "letmein",
    "trustno1",
    "dragon",
    "baseball",
    "iloveyou",
    "master",
    "sunshine",
    "ashley",
    "bailey",
    "shadow",
    "superman",
    "qazwsx"
])

def validate_password_strength(password: str) -> bool:
    if not password or len(password) == 0:
        return False
    if password.lower() in COMMON_COMPROMISED_PASSWORDS:
        return False
    if len(password) < 8:
        return False
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    if not (has_lower and has_upper and has_digit and has_special):
        return False
    return True

if __name__ == '__main__':
    test_passwords = ["Password1!", "password", "Str0ng@Pass", "123456", "MyS3cure!P@ss"]
    results = {pwd: validate_password_strength(pwd) for pwd in test_passwords}
    for pwd, is_valid in results.items():
        print(f"{pwd}: {is_valid}")