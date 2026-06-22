def is_password_compromised(password: str) -> bool:
    common_passwords = {
        "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
        "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "princess",
        "football", "shadow", "superman", "michael", "password1", "123123", "admin",
        "letmein", "welcome", "login", "passw0rd", "hello", "charlie", "donald", "password123",
        "1q2w3e4r", "654321", "121212", "000000", "access", "flower", "hottie", "loveme",
        "zxcvbn", "qwerty123", "mustang", "testing", "batman", "trustno1", "jennifer",
        "hunter2", "1234", "test", "pass", "love", "sexy", "696969", "ashley", "666666",
        "bailey", "daniel", "joshua", "maggie", "ashleigh", "jessica", "nicole", "pepper",
        "ginger", "chelsea", "summer", "robert", "jordan", "daniel", "jonathan", "stephanie",
        "amanda", "joseph", "kyle", "david", "matthew", "anthony", "william", "james",
        "thomas", "charles", "christian", "mark", "steven", "paul", "andrew", "joshua",
        "david", "michael", "daniel", "william", "joseph", "thomas", "christian", "mark",
        "steven", "paul", "andrew", "joshua", "david", "michael", "daniel"
    }
    return password.lower() in common_passwords

def validate_password_strength(password: str) -> bool:
    if not is_password_compromised(password):
        return True
    return False

if __name__ == '__main__':
    result = validate_password_strength("CorrectHorseBatteryStaple")
    print(result)
    
    result2 = validate_password_strength("password")
    print(result2)