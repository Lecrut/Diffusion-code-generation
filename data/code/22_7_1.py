def check_password(password: str) -> bool:
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    for char in password:
        code = ord(char)
        
        lower_mask = (code - 97) & 0xFF
        if lower_mask < 26 and (code & 0xDF) == code:
            has_lower = 1
        
        upper_mask = (code - 65) & 0xFF
        if upper_mask < 26 and (code & 0x40) == 0:
            has_upper = 1
        
        digit_mask = (code - 48) & 0xFF
        if digit_mask < 10:
            has_digit = 1
        
        is_special = 0
        for s_char in special_chars:
            if char == s_char:
                is_special = 1
                break
        if is_special:
            has_special = 1
    
    required = (has_lower << 0) | (has_upper << 1) | (has_digit << 2) | (has_special << 3)
    return required == 15

if __name__ == '__main__':
    test_passwords = [
        "MyPass123!",
        "weakpass",
        "STRONG123",
        "12345678",
        "!@#$%^&*",
        "SecureP@ss2024"
    ]
    
    results = []
    for p in test_passwords:
        results.append(check_password(p))
    
    print(results)