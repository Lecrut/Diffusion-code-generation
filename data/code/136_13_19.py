def evaluate_logic(a: bool, b: bool, c: bool) -> str:
    if a and (not b) or c:
        return 'Decision A'
    elif not a and b and c:
        return 'Decision B'
    else:
        return 'Default Decision'
if __name__ == '__main__':
    result = evaluate_logic(True, False, True)
    print(result)