def validate_password_strength(password: str) -> bool:
    common_weak_passwords = {
        'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', 'master',
        'dragon', '111111', 'baseball', 'iloveyou', 'trustno1', 'sunshine', 'princess',
        'football', 'shadow', 'superman', 'michael', 'password1', '654321', 'qwerty123',
        'letmein', '1q2w3e4r', '121212', 'admin', 'welcome', 'hello', 'charlie', 'donald',
        'login', 'starwars', 'zxcvbn', '000000', 'access', 'flower', 'hottie', 'loveme',
        'mustang', 'trustme', 'amanda', 'ashley', 'bailey', 'cheese', 'chocolate', 'ferrari',
        'ginger', 'hotdog', 'jessica', 'jennifer', 'joshua', 'thomas', 'pepper', 'hunter',
        'andrew', 'harley', 'ranger', 'spider', 'summer', 'tigger', 'robert', 'daniel',
        'ashley', 'nicole', 'bitch', 'angel', 'soccer', 'yankees', 'rangers', 'chelsea',
        'arsenal', 'liverpool', 'manson', 'matthew', '1234', '12345', '123456789', '1234567890',
        '123456789', 'password123', 'letmein1', 'welcome1', 'admin1', 'test', 'guest',
        'default', 'root', 'user', 'pass', 'login1', 'test1', 'guest1', 'user1', 'root1'
    }

    if not password:
        return False

    if password.lower() in common_weak_passwords:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if not (has_upper and has_lower and has_digit):
        return False

    if len(password) < 8:
        return False

    sequential_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    reversed_sequential_chars = sequential_chars[::-1]
    
    has_sequential = False
    for i in range(len(password) - 2):
        char1 = password[i].lower()
        char2 = password[i + 1].lower()
        char3 = password[i + 2].lower()
        
        idx1 = sequential_chars.find(char1)
        idx2 = sequential_chars.find(char2)
        idx3 = sequential_chars.find(char3)
        
        if idx1 != -1 and idx2 != -1 and idx3 != -1:
            if idx2 == idx1 + 1 and idx3 == idx2 + 1:
                has_sequential = True
                break
            
            rev_idx1 = reversed_sequential_chars.find(char1)
            rev_idx2 = reversed_sequential_chars.find(char2)
            rev_idx3 = reversed_sequential_chars.find(char3)
            
            if rev_idx1 != -1 and rev_idx2 != -1 and rev_idx3 != -1:
                if rev_idx2 == rev_idx1 + 1 and rev_idx3 == rev_idx2 + 1:
                    has_sequential = True
                    break

    if has_sequential:
        return False

    return True

if __name__ == '__main__':
    print(validate_password_strength('Str0ng!P@ss'))
    print(validate_password_strength('password'))
    print(validate_password_strength('abc123ABC!'))
    print(validate_password_strength('Abc123'))
    print(validate_password_strength('AaaBbbCCC123!'))