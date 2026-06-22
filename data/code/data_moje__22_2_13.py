class PasswordValidator:
    @staticmethod
    def is_valid(password: str) -> bool:
        if len(password) < 12:
            return False
        
        special_count = 0
        special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")
        for char in password:
            if char in special_chars:
                special_count += 1
        if special_count < 2:
            return False
        
        sequential_keys = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "1234567890",
            "qwer", "wert", "erty", "rtyu", "tyui", "yuio", "uiop",
            "asdf", "sdfg", "dfgh", "fghj", "ghjk", "hjkl",
            "zxcv", "xcvb", "cvbn", "vbnm",
            "0123", "1234", "2345", "3456", "4567", "5678", "6789", "7890"
        ]
        
        password_lower = password.lower()
        for seq in sequential_keys:
            for i in range(len(seq) - 3):
                if seq[i:i+4] in password_lower:
                    return False
        
        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    valid_pass = "Aa1!bB2@cC#"
    invalid_pass = "Short!@#"
    sequential_pass = "Password!@12345678"
    
    result1 = validator.is_valid(valid_pass)
    result2 = validator.is_valid(invalid_pass)
    result3 = validator.is_valid(sequential_pass)
    
    print(result1)
    print(result2)
    print(result3)