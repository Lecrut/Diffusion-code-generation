import operator

def evaluate_conditions(a, b, c, d):
    result_with_operators = operator.and_(operator.or_(a, b), operator.or_(c, d))
    result_with_keywords = (a or b) and (c or d)
    precedence_demo = a or b and c or d
    return {
        "operator_module": result_with_operators,
        "keywords": result_with_keywords,
        "precedence_effect": precedence_demo
    }

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    sample_c = False
    sample_d = True
    output = evaluate_conditions(sample_a, sample_b, sample_c, sample_d)
    print(output)