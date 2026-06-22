def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return True

def compare_two_simple_quantities_now_validate(a, b):
    if not validate_inputs(a, b):
        raise ValueError("Validation failed")
    
    if a > b:
        return "a is greater"
    elif b > a:
        return "b is greater"
    else:
        return "the quantities are equal"

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    try:
        result = compare_two_simple_quantities_now_validate(sample_a, sample_b)
        print(result)
    except ValueError as e:
        print(e)