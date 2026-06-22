def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    return wrapper

@first_element_decorator
def get_data():
    return [42, 84, 168]

if __name__ == '__main__':
    print(get_data())