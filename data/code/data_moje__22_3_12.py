import hashlib

COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "baseball", "iloveyou", "trustno1", "123123", "abc123",
    "password1", "qwerty123", "000000", "1q2w3e4r", "letmein",
    "monkey", "master", "696969", "shadow", "sunshine",
    "princess", "football", "charlie", "access", "thunder",
    "michael", "superman", "jennifer", "joshua", "banana",
    "summer", "love", "ashley", "jessica", "daniel",
    "hunter", "rachel", "samantha", "angel", "nathan"
]

def _build_hash_set(password_list):
    salted_set = set()
    for pwd in password_list:
        normalized = pwd.strip().lower()
        if not normalized:
            continue
        salted_set.add(normalized)
    return salted_set

COMPROMISED_PASSWORDS = _build_hash_set(COMMON_PASSWORDS)

def check_password_strength(password):
    normalized = password.strip().lower()
    if normalized in COMPROMISED_PASSWORDS:
        return False
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    counts = sum([has_upper, has_lower, has_digit, has_special])
    if counts < 3:
        return False
    return True

if __name__ == '__main__':
    test_passwords = ["123456", "MyP@ssw0rd!", "password", "Short!1"]
    for pwd in test_passwords:
        result = check_password_strength(pwd)
        print(result)