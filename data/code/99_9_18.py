import operator

def evaluate_conditions(condition1, condition2, condition3):
    result = (not condition1) and (condition2 or condition3)
    return result

if __name__ == '__main__':
    print(evaluate_conditions(True, False, True))