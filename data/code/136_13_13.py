def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    return (a or b) and not c

if __name__ == '__main__':
    result = evaluate_logic(True, False, True)
    print(result)