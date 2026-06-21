import string

def score_password_strength(password):
    if not password:
        return 0
    
    length = len(password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    diversity_score = sum([has_lower, has_upper, has_digit, has_special])
    
    length_score = min(5, length // 4)
    
    total_score = diversity_score + length_score
    
    return min(10, max(0, total_score))

if __name__ == '__main__':
    print(score_password_strength(""))
    print(score_password_strength("a"))
    print(score_password_strength("password"))
    print(score_password_strength("Passw0rd!"))
    print(score_password_strength("Tr0ub4dor&3"))
    print(score_password_strength("CorrectHorseBatteryStaple!"))