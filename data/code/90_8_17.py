THRESHOLD_A = 5
THRESHOLD_B = 10

def evaluate_or_condition(a, b):
    return a > THRESHOLD_A or b < THRESHOLD_B
if __name__ == '__main__':
    result1 = evaluate_or_condition(6, 9)
    print(result1)
    result2 = evaluate_or_condition(4, 11)
    print(result2)