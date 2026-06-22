import hashlib

COMMON_COMPROMISED_PASSWORDS = [
    "password123",
    "123456",
    "qwerty",
    "letmein",
    "admin",
    "welcome",
    "monkey",
    "dragon",
    "master",
    "login"
]

def check_password_strength(password):
    if password in COMMON_COMPROMISED_PASSWORDS:
        raise ValueError("Password is in the list of common compromised passwords.")
    return True

if __name__ == '__main__':
    test_passwords = ["secureP@ss99", "123456", "MyStr0ng!Pass"]
    results = []
    for pwd in test_passwords:
        try:
            check_password_strength(pwd)
            results.append(f"{pwd}: Valid")
        except ValueError as e:
            results.append(f"{pwd}: Invalid - {e}")
    print(results)