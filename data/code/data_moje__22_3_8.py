def validate_password(password: str) -> bool:
    compromised_passwords = frozenset([
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "trustno1", "dragon",
        "baseball", "iloveyou", "master", "sunshine", "ashley",
        "bailey", "shadow", "123123", "654321", "superman",
        "qazwsx", "michael", "football", "password1", "password123",
        "1234", "12345", "charlie", "donald", "hello", "loveme",
        "access", "1q2w3e4r", "welcome", "qwerty123", "admin",
        "login", "princess", "starwars", "solo", "mustang", "jordan",
        "passw0rd", "hello123", "1234567890", "111111", "000000",
        "121212", "test", "guest", "root", "admin123", "changeme",
        "master123", "administrator", "user", "password!", "p@ssword",
        "pa$$word", "Pass1234", "Password1", "welcome1", "Summer2023",
        "Winter2023", "Spring2023", "Fall2023", "2023", "2024",
        "123qwe", "abc123456", "123456789", "1234567890", "12345678910",
        "666666", "123321", "112233", "zxcvbnm", "696969",
        "hello", "charlie", "donald", "password123", "test",
        "admin", "login", "welcome", "starwars", "football",
        "soccer", "hockey", "batman", "pepper", "joshua",
        "jordan", "hunter", "freedom", "princess", "summer",
        "flower", "robert", "thomas", "secret", "amanda",
        "daniel", "jessica", "andrew", "michael", "jennifer",
        "william", "joshua1", "nicole", "michelle", "tigger",
        "sunflower", "buster", "cookie", "george", "computer",
        "jackson", "killer", "ginger"
    ])
    return password not in compromised_passwords

def get_validation_status(password: str) -> str:
    is_valid = validate_password(password)
    if is_valid:
        return "Valid"
    return "Invalid"

if __name__ == '__main__':
    test_passwords = ["password", "MyS3cur3P@ss!", "123456", "StrongPassword123!", "qwerty", "ComplexP@ssw0rd#2024"]
    for pwd in test_passwords:
        status = get_validation_status(pwd)
        print(f"{pwd}: {status}")