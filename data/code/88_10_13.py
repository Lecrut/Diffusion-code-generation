def validate_conditions(condition_a, condition_b):
    if not isinstance(condition_a, bool) or not isinstance(condition_b, bool):
        raise ValueError("Both conditions must be boolean values.")
    return True

def check_conditions(condition_a, condition_b):
    if not validate_conditions(condition_a, condition_b):
        return None
    return condition_a and condition_b

if __name__ == '__main__':
    condition_a = True
    condition_b = False
    result = check_conditions(condition_a, condition_b)
    print(result)