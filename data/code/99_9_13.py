import operator

def evaluate_conditions(condition1, condition2):
    return (condition1 and condition2) or not (condition1 or condition2)

if __name__ == '__main__':
    print(evaluate_conditions(True, False))