COMMON_COMPROMISED_PASSWORDS = frozenset([
    "123456",
    "password",
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
    "passw0rd",
    "shadow",
    "123123",
    "654321",
    "superman",
    "qazwsx",
    "michael",
    "football",
    "password1",
    "password123"
])

def is_password_compromised(password: str) -> bool:
    if not isinstance(password, str):
        return False
    return password in COMMON_COMPROMISED_PASSWORDS

if __name__ == '__main__':
    test_cases = ["securePass99", "123456", "qwerty", "MyStr0ngP@ss"]
    results = []
    for pwd in test_cases:
        results.append(is_password_compromised(pwd))
    print(results)