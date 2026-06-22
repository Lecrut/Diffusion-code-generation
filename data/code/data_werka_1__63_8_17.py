def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    return wrapper

@first_element_decorator
def retrieve_items():
    return ['apple', 'banana', 'cherry']

if __name__ == '__main__':
    print(retrieve_items())