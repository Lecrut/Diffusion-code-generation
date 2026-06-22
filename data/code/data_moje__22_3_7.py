def is_password_compromised(password):
    compromised_passwords = {
        "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
        "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine",
        "princess", "football", "shadow", "superman", "michael", "login",
        "admin", "welcome", "hello", "charlie", "donald", "password1",
        "123456789", "654321", "000000", "1234567", "qwerty123", "1234567890",
        "987654321", "letmein", "admin123", "password123", "1234", "12345",
        "1234567890", "123123", "666666", "abc123", "111111", "12345678"
    }
    return password.lower() in compromised_passwords

if __name__ == '__main__':
    print(is_password_compromised("password"))
    print(is_password_compromised("SecureP@ssw0rd!"))
    print(is_password_compromised("qwerty"))
    print(is_password_compromised("MyUniqueP@ss"))