import operator

def evaluate_conditions(a: bool, b: bool, c: bool) -> dict:
    and_result = operator.and_(a, b)
    or_result = operator.or_(and_result, c)
    
    precedence_and = a and b
    precedence_or = precedence_and or c
    
    mixed_precedence = a and b or c
    
    return {
        "operator_and": and_result,
        "operator_or": or_result,
        "logical_and": precedence_and,
        "logical_or": precedence_or,
        "mixed_precedence": mixed_precedence
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    
    results = evaluate_conditions(sample_a, sample_b, sample_c)
    
    print(results["operator_and"])
    print(results["operator_or"])
    print(results["logical_and"])
    print(results["logical_or"])
    print(results["mixed_precedence"])