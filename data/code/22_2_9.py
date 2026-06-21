class PasswordValidator:
    SPECIAL_CHARS = set("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")
    KEYBOARD_PATTERNS = ["qwerty", "asdfgh", "zxcvbn", "123456", "qazwsx", "wsxedc", "edcrfv", "rfvtgb", "tgbyhn", "yhnujm", "qwert", "asdfg", "zxcvb", "1234", "2345", "3456", "4567", "5678", "6789", "7890", "0987", "9876", "8765", "7654", "6543", "5432", "4321", "qwe", "asd", "zxc", "123"]

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False
        
        special_count = 0
        for char in password:
            if char in PasswordValidator.SPECIAL_CHARS:
                special_count += 1
                if special_count >= 2:
                    break
        else:
            return False
        
        if special_count < 2:
            return False
        
        password_lower = password.lower()
        for pattern in PasswordValidator.KEYBOARD_PATTERNS:
            if pattern in password_lower:
                return False
        
        for i in range(len(password) - 2):
            char1 = ord(password[i].lower())
            char2 = ord(password[i+1].lower())
            char3 = ord(password[i+2].lower())
            
            if char1 == char2 == char3:
                return False
            
            if char2 - char1 == 1 and char3 - char2 == 1:
                return False
            
            if char1 - char2 == 1 and char2 - char3 == 1:
                return False
        
        return True

if __name__ == '__main__':
    test_passwords = [
        "ValidPass@#123456",
        "Weak1!",
        "NoSpecialHere123",
        "HasTwoSpecial!!123",
        "Sequential12345!@",
        "PatternQWERTY!@123"
    ]
    
    results = []
    for pwd in test_passwords:
        result = PasswordValidator.validate(pwd)
        results.append(f"{pwd}: {result}")
    
    for r in results:
        print(r)