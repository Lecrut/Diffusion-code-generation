def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    try:
        if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool):
            raise ValueError("All inputs must be boolean values.")
        return (a and b) or not c
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    print(evaluate_logic(True, False, True))
    print(evaluate_logic(False, False, False))
    print(evaluate_logic(True, True, False))
    print(evaluate_logic(False, True, True))