def evaluate_conditions():
    condition1 = True
    condition2 = False
    condition3 = True

    result = "All conditions met" if condition1 and condition2 and condition3 else "Conditions not met"
    return result

if __name__ == '__main__':
    print(evaluate_conditions())