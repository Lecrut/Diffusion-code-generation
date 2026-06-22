def validate_bool(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def evaluate_logic(a, b, c):
    a = validate_bool(a)
    b = validate_bool(b)
    c = validate_bool(c)
    
    precedence_result = a and b or c
    explicit_paren_result = (a and b) or c
    different_grouping = a and (b or c)
    
    return {
        "input": (a, b, c),
        "a_and_b_or_c": precedence_result,
        "explicit_paren": explicit_paren_result,
        "different_grouping": different_grouping
    }

if __name__ == '__main__':
    x = True
    y = False
    z = True
    result = evaluate_logic(x, y, z)
    print(result)