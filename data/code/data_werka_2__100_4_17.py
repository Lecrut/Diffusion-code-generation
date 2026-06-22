from enum import Enum

class ComparisonOutcome(Enum):
    GREATER = 1
    NOT_GREATER = 2

MIN_INT = -2147483648
MAX_INT = 2147483647

def determine_greater(x: int, y: int) -> bool:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Inputs must be integers")
    if x < MIN_INT or x > MAX_INT or y < MIN_INT or y > MAX_INT:
        raise ValueError("Inputs out of integer range")
    if x > y:
        return True
    return False

if __name__ == '__main__':
    val_a = 42
    val_b = 17
    outcome_enum = ComparisonOutcome.GREATER if determine_greater(val_a, val_b) else ComparisonOutcome.NOT_GREATER
    print(outcome_enum.value)