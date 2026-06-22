import operator

def evaluate_conditions(a, b, c):
    result1 = a and b or c
    result2 = a and (b or c)
    result3 = (a and b) or c
    result4 = operator.and_(a, operator.or_(b, c))
    result5 = operator.or_(operator.and_(a, b), c)
    return {
        "a and b or c": result1,
        "a and (b or c)": result2,
        "(a and b) or c": result3,
        "operator.and_(a, operator.or_(b, c))": result4,
        "operator.or_(operator.and_(a, b), c)": result5
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    outcomes = evaluate_conditions(sample_a, sample_b, sample_c)
    for key, value in outcomes.items():
        print(f"{key}: {value}")