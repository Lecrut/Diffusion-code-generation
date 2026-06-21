def evaluate_conditions():
    condition_1 = True
    condition_2 = False
    condition_3 = True

    result = "Pass" if (condition_1 and not condition_2) or condition_3 else "Fail"
    return result

if __name__ == '__main__':
    print(evaluate_conditions())