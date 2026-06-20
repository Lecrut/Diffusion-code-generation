def evaluate_conditions(a: bool, b: bool) -> bool:
    return a and b

def validate_inputs(a: bool, b: bool):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

if __name__ == '__main__':
    try:
        validate_inputs(True, False)
        result = evaluate_conditions(True, False)
        print(f'AND Result: {result}')
    except ValueError as e:
        print(e)