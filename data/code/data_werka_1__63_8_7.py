def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    return wrapper

@first_element_decorator
def process_data():
    return [10, 20, 30, 40]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45]
    print(process_data())