def evaluate_conditions(a, b, c):
    result_with_precedence = a and b or c
    result_with_parentheses = (a and b) or c
    result_different_precedence = a and (b or c)
    return {
        "a": a,
        "b": b,
        "c": c,
        "a_and_b_or_c": result_with_precedence,
        "(a_and_b)_or_c": result_with_parentheses,
        "a_and_(b_or_c)": result_different_precedence
    }

if __name__ == '__main__':
    sample_values = evaluate_conditions(True, False, True)
    print(sample_values)