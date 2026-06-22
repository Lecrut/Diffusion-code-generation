import operator

def evaluate_conditions(a, b, c):
    result_with_operator = operator.and_(operator.or_(a, b), c)
    result_with_keywords = (a or b) and c
    precedence_demo = a or b and c
    return result_with_operator, result_with_keywords, precedence_demo

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = False
    res1, res2, res3 = evaluate_conditions(val_a, val_b, val_c)
    print(res1)
    print(res2)
    print(res3)