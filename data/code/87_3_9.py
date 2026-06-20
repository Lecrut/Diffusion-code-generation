CONDITION_A = True
CONDITION_B = False
CONDITION_C = True

def evaluate_expression(a=CONDITION_A, b=CONDITION_B, c=CONDITION_C):
    return (a and b) or c

if __name__ == '__main__':
    result = evaluate_expression()
    print(result)