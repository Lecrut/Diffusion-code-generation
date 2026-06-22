def first_element_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    return wrapper

@first_element_decorator
def sample_function(data):
    return data
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(sample_function(sample_data))
    empty_list = []
    print(sample_function(empty_list))
    non_list_input = 'Hello'
    print(sample_function(non_list_input))