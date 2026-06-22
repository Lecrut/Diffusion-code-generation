import operator

def evaluate_conditions(a, b, c):
    result_with_precedence = (a and b) or c
    result_with_operators = operator.or_(operator.and_(a, b), c)
    return result_with_precedence, result_with_operators

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    res1, res2 = evaluate_conditions(val_a, val_b, val_c)
    print(res1, res2)