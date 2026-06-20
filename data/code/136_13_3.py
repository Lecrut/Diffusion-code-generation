def evaluate_logic(x: bool, y: bool) -> str:
    if x and (not y):
        return 'Option 1'
    elif not x and y:
        return 'Option 2'
    elif x or y:
        return 'Both Set'
    else:
        return 'Neither'
if __name__ == '__main__':
    result1 = evaluate_logic(True, False)
    print(result1)
    result2 = evaluate_logic(False, True)
    print(result2)
    result3 = evaluate_logic(True, True)
    print(result3)
    result4 = evaluate_logic(False, False)
    print(result4)