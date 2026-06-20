def evaluate_logic(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean")
    return int(a) & int(b)

if __name__ == '__main__':
    print(evaluate_logic(True, False))