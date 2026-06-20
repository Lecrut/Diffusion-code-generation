def evaluate_logic(a: bool, b: bool, c: bool) -> str:
    if a and not b or c:
        return "Decision A"
    elif b and c:
        return "Decision B"
    else:
        return "Default Decision"

if __name__ == '__main__':
    print(evaluate_logic(True, False, True))