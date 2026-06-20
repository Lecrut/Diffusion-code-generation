def is_valid_input(a: bool, b: bool) -> bool:
    return isinstance(a, bool) and isinstance(b, bool)

def evaluate_logic(a: bool, b: bool) -> str:
    if not is_valid_input(a, b):
        raise ValueError("Inputs must be boolean values.")
    
    if a and (not b):
        return 'Decision A'
    elif not a and b:
        return 'Decision B'
    else:
        return 'No Decision'

if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))