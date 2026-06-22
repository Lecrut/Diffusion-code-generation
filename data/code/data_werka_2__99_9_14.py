import operator

def evaluate_boolean_conditions(a: bool, b: bool, c: bool) -> dict:
    and_result = a and b and c
    or_result = a or b or c
    mixed_precedence = a and b or c
    mixed_precedence_alternate = (a and b) or c
    mixed_precedence_parenthesized = a and (b or c)
    
    return {
        "and_all": and_result,
        "or_any": or_result,
        "mixed_no_parens": mixed_precedence,
        "mixed_explicit_and_first": mixed_precedence_alternate,
        "mixed_explicit_or_first": mixed_precedence_parenthesized,
        "operator_and": operator.and_(a, operator.and_(b, c)),
        "operator_or": operator.or_(a, operator.or_(b, c))
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    
    results = evaluate_boolean_conditions(sample_a, sample_b, sample_c)
    
    for key, value in results.items():
        print(f"{key}: {value}")