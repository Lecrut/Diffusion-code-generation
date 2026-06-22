def validate_password(password):
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
    
    common_weak = ["password", "123456", "12345678", "qwerty", "abc123", "monkey", "master", "dragon", "login", "princess"]
    if password.lower() in common_weak:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    
    sequential_pairs = [
        "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl",
        "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv",
        "uvw", "vwx", "wxy", "xyz",
        "012", "123", "234", "345", "456", "567", "678", "789", "890",
        "ABC", "BCD", "CDE", "DEF", "EFG", "FGH", "GHI", "HIJ", "IJK", "JKL",
        "KLM", "LMN", "MNO", "NOP", "OPQ", "PQR", "QRS", "RST", "STU", "TUV",
        "UVW", "VWX", "WXY", "XYZ"
    ]
    
    lower_pwd = password.lower()
    for seq in sequential_pairs:
        if seq in lower_pwd:
            return False
            
    repeated_chars = set()
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
            
    return True

if __name__ == '__main__':
    print(validate_password("Str0ng!Pass"))
    print(validate_password("password123!"))
    print(validate_password("abc123ABC!"))
    print(validate_password("aaaAAA123!"))
    print(validate_password("Short!A1"))