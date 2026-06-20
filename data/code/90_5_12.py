def or_condition_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, bool) and len(result) != 2:
            raise ValueError("Function must return a boolean or a tuple of two booleans")
        if isinstance(result, bool):
            return result
        else:
            condition1, condition2 = result
            if not isinstance(condition1, bool) or not isinstance(condition2, bool):
                raise ValueError("Both elements in the tuple must be booleans")
            return condition1 or condition2
    return wrapper

@or_condition_decorator
def check_or_conditions(input_data):
    return input_data

if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False)
    ]
    output = check_or_conditions(sample_data)
    print(output)