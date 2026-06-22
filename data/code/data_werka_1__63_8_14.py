def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[0] if isinstance(result, list) and result else None
    return wrapper

@first_element_decorator
def retrieve_list():
    return [5, 15, 25, 35, 45]

if __name__ == '__main__':
    print(retrieve_list())