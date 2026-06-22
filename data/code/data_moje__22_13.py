import math
import string
import enum
import dataclasses

class ValidationResult(enum.Enum):
    VALID = "valid"
    INVALID = "invalid"

@dataclasses.dataclass
class PasswordEntropyResult:
    is_valid: bool
    entropy_bits: float
    length: int
    character_set_size: int
    failure_reasons: list

def calculate_password_entropy(password: str, min_entropy_bits: float = 60.0) -> PasswordEntropyResult:
    length = len(password)
    failure_reasons = []
    
    if length == 0:
        return PasswordEntropyResult(
            is_valid=False,
            entropy_bits=0.0,
            length=0,
            character_set_size=0,
            failure_reasons=["Password cannot be empty"]
        )
    
    char_pool = 0
    if any(c in string.ascii_lowercase for c in password):
        char_pool += 26
    if any(c in string.ascii_uppercase for c in password):
        char_pool += 26
    if any(c in string.digits for c in password):
        char_pool += 10
    if any(c in string.punctuation for c in password):
        char_pool += 32
    
    if char_pool == 0:
        char_pool = 1
    
    entropy_bits = length * math.log2(char_pool)
    
    if entropy_bits < min_entropy_bits:
        failure_reasons.append(f"Entropy {entropy_bits:.2f} bits is below threshold {min_entropy_bits} bits")
    
    if length < 8:
        failure_reasons.append("Password length is less than 8 characters")
    
    is_valid = len(failure_reasons) == 0
    
    return PasswordEntropyResult(
        is_valid=is_valid,
        entropy_bits=entropy_bits,
        length=length,
        character_set_size=char_pool,
        failure_reasons=failure_reasons
    )

if __name__ == '__main__':
    result_strong = calculate_password_entropy("Correct-Horse-Battery-Staple!123")
    print(result_strong)
    
    result_weak = calculate_password_entropy("abc123")
    print(result_weak)
    
    result_empty = calculate_password_entropy("")
    print(result_empty)
    
    result_medium = calculate_password_entropy("Password1!")
    print(result_medium)