def is_password_compromised(password):
    common_compromised = {
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234567890", "1234567", "password1", "000000",
        "1234", "111111", "12345678910", "121212", "access",
        "666666", "abc123", "monkey", "123123", "654321",
        "letmein", "trustno1", "dragon", "baseball", "iloveyou",
        "master", "sunshine", "ashley", "bailey", "shadow",
        "123qwe", "696969", "123321", "112233", "qwerty123",
        "zxcvbnm", "passw0rd", "hello", "charlie", "donald",
        "password123", "test", "admin", "login", "welcome",
        "starwars", "football", "soccer", "hockey", "batman",
        "pepper", "joshua", "jordan", "hunter", "freedom",
        "princess", "summer", "flower", "robert", "thomas",
        "secret", "amanda", "daniel", "jessica", "andrew",
        "michael", "jennifer", "william", "joshua1", "nicole",
        "michelle", "tigger", "sunflower", "buster", "cookie",
        "george", "computer", "jackson", "killer", "ginger",
        "heather", "yankees", "phoenix", "ranger", "diamond"
    }
    normalized = password.strip().lower()
    return normalized in common_compromised

if __name__ == '__main__':
    test_passwords = ["password", "MyS3cureP@ss!", "123456", "Unicorn42!", "admin"]
    results = []
    for pwd in test_passwords:
        is_compromised = is_password_compromised(pwd)
        results.append((pwd, is_compromised))
    print(results)