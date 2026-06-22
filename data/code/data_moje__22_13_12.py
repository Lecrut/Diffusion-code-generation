import math
import string

PASSWORD_MIN_LENGTH = 8
CHAR_SETS = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)

class PasswordEvaluationResult:
    def __init__(self, is_valid, entropy_bits, length, diversity_count, failure_reasons):
        self.is_valid = is_valid
        self.entropy_bits = entropy_bits
        self.length = length
        self.diversity_count = diversity_count
        self.failure_reasons = failure_reasons

    def __repr__(self):
        return (
            f"PasswordEvaluationResult(is_valid={self.is_valid}, "
            f"entropy_bits={self.entropy_bits:.2f}, "
            f"length={self.length}, "
            f"diversity_count={self.diversity_count}, "
            f"failure_reasons={self.failure_reasons})"
        )

def evaluate_password_entropy(password):
    length = len(password)
    diversity_count = 0
    for char_set in CHAR_SETS:
        if any(char in char_set for char in password):
            diversity_count += 1

    charset_size = 0
    for char_set in CHAR_SETS:
        if any(char in char_set for char in password):
            charset_size += len(char_set)

    if charset_size == 0:
        entropy_bits = 0.0
    else:
        entropy_bits = length * math.log2(charset_size)

    failure_reasons = []
    if length < PASSWORD_MIN_LENGTH:
        failure_reasons.append("too_short")
    if diversity_count < 2:
        failure_reasons.append("insufficient_character_diversity")
    if entropy_bits < 60:
        failure_reasons.append("low_entropy")

    is_valid = (length >= PASSWORD_MIN_LENGTH and diversity_count >= 2 and entropy_bits >= 60)

    return PasswordEvaluationResult(
        is_valid=is_valid,
        entropy_bits=entropy_bits,
        length=length,
        diversity_count=diversity_count,
        failure_reasons=failure_reasons
    )

if __name__ == '__main__':
    result = evaluate_password_entropy("Str0ng!Pass#2023")
    print(result)
    
    weak_result = evaluate_password_entropy("abc")
    print(weak_result)