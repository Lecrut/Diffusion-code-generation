from enum import Enum

class Relation(Enum):
    GREATER = 1
    EQUAL = 2
    LESS = 3

COMPARE_RESULT = {
    True: Relation.GREATER,
    False: Relation.EQUAL
}

def check_greater(x: int, y: int) -> bool:
    if x > y:
        result_value = True
    else:
        result_value = False
    return result_value

if __name__ == '__main__':
    a = 10
    b = 20
    outcome = check_greater(a, b)
    print(outcome)