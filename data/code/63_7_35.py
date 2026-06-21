def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and result:
            return result[0]
        raise ValueError("Function did not return a non-empty list")
    return wrapper

@first_element_decorator
def sample_function():
    return [10, 11, 12]

if __name__ == '__main__':
    try:
        print(sample_function())
    except ValueError as e:
        print(e)