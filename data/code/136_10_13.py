def evaluate_logical_operators(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")
    
    and_result = a and b
    or_result = a or b
    not_a_result = not a
    
    return and_result, or_result, not_a_result

def main():
    sample_a = True
    sample_b = False
    try:
        and_result, or_result, not_a_result = evaluate_logical_operators(sample_a, sample_b)
        print(f"a: {sample_a}")
        print(f"b: {sample_b}")
        print(f"a AND b: {and_result}")
        print(f"a OR b: {or_result}")
        print(f"NOT a: {not_a_result}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()