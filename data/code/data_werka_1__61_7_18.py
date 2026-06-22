def retrieve_element(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and 0 <= index < len(result):
                return result[index]
            else:
                raise ValueError("Invalid index or non-list result")
        return wrapper
    return decorator

@retrieve_element(3)
def get_data():
    return [100, 200, 300, 400, 500]

if __name__ == '__main__':
    try:
        element = get_data()
        print(element)
    except ValueError as e:
        print(e)