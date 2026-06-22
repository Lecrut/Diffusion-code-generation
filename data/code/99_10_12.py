def evaluate_complex_expression(a, b, c, d):
    if not all(isinstance(x, bool) for x in (a, b, c, d)):
        raise ValueError("All inputs must be boolean values")
    
    standard_precedence = a and b or c and d
    explicit_grouping_1 = (a and b) or (c and d)
    explicit_grouping_2 = a and (b or c) and d
    negation_complex = not (a or b) and c or d
    mixed_negation = (not a and b) or (c and not d)
    deep_parentheses = ((a and not b) or (c and d)) and (not a or b)
    
    results = {
        "a and b or c and d": standard_precedence,
        "(a and b) or (c and d)": explicit_grouping_1,
        "a and (b or c) and d": explicit_grouping_2,
        "not (a or b) and c or d": negation_complex,
        "(not a and b) or (c and not d)": mixed_negation,
        "((a and not b) or (c and d)) and (not a or b)": deep_parentheses
    }
    return results

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    
    computed_results = evaluate_complex_expression(sample_a, sample_b, sample_c, sample_d)
    
    print(computed_results)