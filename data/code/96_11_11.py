def evaluate_nested_structure(nested):
    if isinstance(nested, list):
        for item in nested:
            if evaluate_nested_structure(item):
                return True
    elif isinstance(nested, bool):
        return nested
    return False

if __name__ == '__main__':
    sample = [[False, [True, False]], [False, False]]
    print(evaluate_nested_structure(sample))