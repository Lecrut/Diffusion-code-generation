def evaluate_logic(x: bool, y: bool, z: bool) -> str:
    decision_a = x and not y and z
    decision_b = not x and y and not z
    if decision_a:
        return "Decision A"
    elif decision_b:
        return "Decision B"
    else:
        return "No Decision"

if __name__ == '__main__':
    result1 = evaluate_logic(True, False, True)
    print(result1)
    result2 = evaluate_logic(False, True, False)
    print(result2)
    result3 = evaluate_logic(True, True, False)
    print(result3)
    result4 = evaluate_logic(False, False, True)
    print(result4)