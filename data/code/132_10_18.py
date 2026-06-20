LOGICAL_AND = lambda x, y: x and y
LOGICAL_NOT = lambda x: not x

def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    return LOGICAL_AND(a, b) or LOGICAL_NOT(c)

if __name__ == '__main__':
    print(evaluate_logic(True, False, True))
    print(evaluate_logic(False, False, False))
    print(evaluate_logic(True, True, False))
    print(evaluate_logic(False, True, True))