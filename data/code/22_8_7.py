def validate_password_strength(password):
    if len(password) < 8:
        return False
    common_words = [
        "password", "123456", "qwerty", "abc123", "monkey", "master",
        "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine",
        "ashley", "football", "shadow", "123123", "654321", "superman",
        "qazwsx", "michael", "login", "letmein", "admin", "welcome",
        "hello", "charlie", "donald", "password1", "696969", "access"
    ]
    lower_password = password.lower()
    for word in common_words:
        if word in lower_password:
            return False
    return True

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "password123",
        "secureP@ssw0rd",
        "abcdefgh",
        "MyStr0ng!Pass",
        "qwerty1234"
    ]
    results = []
    for pwd in sample_passwords:
        result = validate_password_strength(pwd)
        results.append((pwd, result))
    for pwd, is_valid in results:
        print((pwd, is_valid))