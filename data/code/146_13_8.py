def evaluate_conditions():
    condition1 = True
    condition2 = False
    condition3 = True

    result = "Pass" if (condition1 and not condition2) or (condition3 and condition2) else "Fail"
    return result

if __name__ == '__main__':
    print(evaluate_conditions())