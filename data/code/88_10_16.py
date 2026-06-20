def check_conditions(condition_a, condition_b):
    if not isinstance(condition_a, bool) or not isinstance(condition_b, bool):
        raise ValueError("Both arguments must be boolean values.")
    
    return condition_a and condition_b

if __name__ == '__main__':
    result = check_conditions(True, False)
    print(result)