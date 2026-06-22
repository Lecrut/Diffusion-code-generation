def validate_password_strength(password: str) -> bool:
    common_passwords = {
        "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein",
        "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine", "ashley", "bailey",
        "shadow", "123123", "654321", "superman", "qazwsx", "michael", "football", "password1",
        "password123", "1234", "12345", "charlie", "donald", "hello", "loveme", "access",
        "1q2w3e4r", "welcome", "qwerty123", "admin", "login", "princess", "starwars", "solo",
        "mustang", "jordan", "passw0rd", "hello123", "1234567890", "111111", "000000", "121212",
        "test", "guest", "root", "admin123", "changeme", "master123", "administrator", "user",
        "password!", "p@ssword", "pa$$word", "Pass1234", "Password1", "welcome1", "Summer2023",
        "Winter2023", "Spring2023", "Fall2023", "2023", "2024", "123qwe", "abc123456",
        "123456789", "00000000", "12121212", "242424", "88888888", "666666", "secret",
        "monkey123", "iloveu", "batman", "trustno1", "access143", "1111", "2222", "3333",
        "4444", "5555", "6666", "7777", "8888", "9999", "0000", "pass", "login1", "user1"
    }
    normalized_password = password.lower().strip()
    is_compromised = normalized_password in common_passwords
    return not is_compromised

if __name__ == '__main__':
    sample_passwords = [
        "password", 
        "MyS3cur3P@ss!", 
        "123456", 
        "StrongPassword123!", 
        "qwerty", 
        "ComplexP@ssw0rd#2024"
    ]
    for current_password in sample_passwords:
        is_valid = validate_password_strength(current_password)
        print(f"{current_password}: {is_valid}")