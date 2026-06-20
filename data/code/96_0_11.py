def evaluate_nested_logic(a, b, c, d):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
        raise ValueError("All inputs must be boolean values")
    
    return (a and b) or (c and not d)

if __name__ == '__main__':
    try:
        result = evaluate_nested_logic(True, False, True, False)
        print(result)
    except ValueError as e:
        print(e)