def first_element_decorator(func):
    def validate_and_wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, list):
            raise ValueError("The function did not return a list.")
        if len(result) == 0:
            raise ValueError("The returned list is empty.")
        return result[0]
    return validate_and_wrap

@first_element_decorator
def sample_function():
    return [10, 20, 30]

if __name__ == '__main__':
    try:
        print(sample_function())
    except ValueError as e:
        print(e)