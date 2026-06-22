from enum import Enum

class ComparisonResult(Enum):
    GREATER = 1
    NOT_GREATER = 2

RELATION_MAP = {
    True: ComparisonResult.GREATER,
    False: ComparisonResult.NOT_GREATER
}

def determine_greater(x: int, y: int) -> ComparisonResult:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Inputs must be integers")
    is_greater = x > y
    return RELATION_MAP[is_greater]

if __name__ == '__main__':
    a = 42
    b = 17
    outcome = determine_greater(a, b)
    print(outcome.value)