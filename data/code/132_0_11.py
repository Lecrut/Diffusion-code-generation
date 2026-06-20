def validate_input(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")

def evaluate_logic(a, b):
    validate_input(a, b)
    return a & b

if __name__ == '__main__':
    print(evaluate_logic(True, False))