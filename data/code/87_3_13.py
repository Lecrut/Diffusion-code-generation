CONDITION_A = True
CONDITION_B = False
CONDITION_C = True

def evaluate_expression():
    return (CONDITION_A and CONDITION_B) or CONDITION_C

if __name__ == '__main__':
    result = evaluate_expression()
    print(result)