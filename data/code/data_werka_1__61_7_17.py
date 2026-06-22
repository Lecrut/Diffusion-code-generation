def element_extractor(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if isinstance(func_result, list) and 0 <= index < len(func_result):
                return func_result[index]
            else:
                raise ValueError("Invalid index or result is not a list")
        return wrapper
    return decorator

@element_extractor(3)
def fetch_elements():
    return [15, 25, 35, 45, 55]

if __name__ == '__main__':
    try:
        print(fetch_elements())
    except Exception as e:
        print(e)