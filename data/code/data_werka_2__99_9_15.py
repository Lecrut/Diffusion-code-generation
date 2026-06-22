def evaluate_conditions(a, b, c):
    result_with_parentheses = (a and b) or c
    result_without_parentheses = a and b or c
    return {
        "with_parentheses": result_with_parentheses,
        "without_parentheses": result_without_parentheses,
        "precedence_explanation": "and binds tighter than or, so a and b or c is parsed as (a and b) or c"
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    outcome = evaluate_conditions(sample_a, sample_b, sample_c)
    print(outcome)