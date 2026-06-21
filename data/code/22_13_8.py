import math
import string
import dataclasses
import typing

@dataclasses.dataclass
class PasswordResult:
    valid: bool
    entropy: float
    length: int
    charset_size: int
    reasons: list[str]

def evaluate_password_entropy(password: str, min_entropy: float = 50.0) -> PasswordResult:
    reasons = []
    length = len(password)
    
    if length == 0:
        charset_size = 0
        entropy = 0.0
        reasons.append("Password is empty")
    else:
        has_lower = False
        has_upper = False
        has_digit = False
        has_symbol = False
        
        for char in password:
            if char in string.ascii_lowercase:
                has_lower = True
            elif char in string.ascii_uppercase:
                has_upper = True
            elif char in string.digits:
                has_digit = True
            elif char in string.punctuation or char in string.whitespace:
                has_symbol = True
        
        charset_size = 0
        if has_lower:
            charset_size += 26
        if has_upper:
            charset_size += 26
        if has_digit:
            charset_size += 10
        if has_symbol:
            charset_size += 33
        
        if charset_size == 0:
            entropy = 0.0
            reasons.append("No valid characters detected")
        else:
            entropy = length * math.log2(charset_size)
        
        if length < 8:
            reasons.append("Password length is less than 8")
        
        if entropy < min_entropy:
            reasons.append(f"Entropy {entropy:.2f} is below threshold {min_entropy}")
            
    valid = len(reasons) == 0
    return PasswordResult(
        valid=valid,
        entropy=entropy,
        length=length,
        charset_size=charset_size,
        reasons=reasons
    )

if __name__ == '__main__':
    test_passwords = [
        "short1",
        "StrongP@ssw0rd123",
        "aaaaaaaaaa",
        "MyC0mpl3x#P@ss"
    ]
    
    for pwd in test_passwords:
        result = evaluate_password_entropy(pwd, 50.0)
        print(result)