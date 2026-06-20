def or_condition_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not any(result):
            raise ValueError("No condition satisfied")
        return result
    return wrapper

@or_condition_decorator
def check_or_conditions(list_of_tuples):
    result = []
    for conditions in list_of_tuples:
        if conditions[0] or conditions[1]:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False)
    ]
    try:
        output = check_or_conditions(sample_data)
        print(output)
    except ValueError as e:
        print(e)