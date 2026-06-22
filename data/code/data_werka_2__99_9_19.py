import operator

def evaluate_conditions(a, b, c):
    result_with_and_or = (a and b) or c
    result_with_operator = operator.or_(operator.and_(a, b), c)
    result_precedence_demo = a and (b or c)
    return result_with_and_or, result_with_operator, result_precedence_demo

if __name__ == '__main__':
    x = True
    y = False
    z = True
    res1, res2, res3 = evaluate_conditions(x, y, z)
    print(res1)
    print(res2)
    print(res3)