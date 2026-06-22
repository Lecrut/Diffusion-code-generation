import operator

def evaluate_conditions(a, b, c):
    result_with_precedence = a and b or c
    result_with_parentheses = (a and b) or c
    result_with_different_parentheses = a and (b or c)
    return {
        "a": a,
        "b": b,
        "c": c,
        "a_and_b_or_c": result_with_precedence,
        "(a_and_b)_or_c": result_with_parentheses,
        "a_and_(b_or_c)": result_with_different_parentheses
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    
    output = evaluate_conditions(sample_a, sample_b, sample_c)
    print(output)