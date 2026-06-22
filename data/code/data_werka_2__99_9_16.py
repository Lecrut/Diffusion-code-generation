import operator

def evaluate_conditions(a: bool, b: bool, c: bool) -> dict:
    result_and = a and b and c
    result_or = a or b or c
    result_precedence_1 = a and (b or c)
    result_precedence_2 = (a and b) or c
    result_operator_and = operator.and_(a, operator.and_(b, c))
    result_operator_or = operator.or_(a, operator.or_(b, c))
    
    return {
        "a": a,
        "b": b,
        "c": c,
        "a_and_b_and_c": result_and,
        "a_or_b_or_c": result_or,
        "a_and_b_or_c": result_precedence_1,
        "(a_and_b)_or_c": result_precedence_2,
        "operator_and": result_operator_and,
        "operator_or": result_operator_or
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    
    output = evaluate_conditions(sample_a, sample_b, sample_c)
    print(output)