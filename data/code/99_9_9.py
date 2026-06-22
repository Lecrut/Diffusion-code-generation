import operator

def evaluate_conditions(a, b, c):
    result_with_precedence = (a and b) or c
    result_with_operator = operator.or_(operator.and_(a, b), c)
    return {
        "logical_and_or": result_with_precedence,
        "operator_module": result_with_operator,
        "are_equal": result_with_precedence == result_with_operator
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    outcome = evaluate_conditions(sample_a, sample_b, sample_c)
    print(outcome)