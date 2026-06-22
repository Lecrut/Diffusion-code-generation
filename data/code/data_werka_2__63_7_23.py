def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        else:
            raise ValueError("The function did not return a non-empty list.")
    return wrapper

@first_element_decorator
def sample_function():
    return [1, 2, 3]

if __name__ == '__main__':
    print(sample_function())