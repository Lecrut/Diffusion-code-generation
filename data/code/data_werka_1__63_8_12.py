def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    return wrapper

@first_element_decorator
def process_data():
    return [5, 10, 15, 20]

if __name__ == '__main__':
    print(process_data())