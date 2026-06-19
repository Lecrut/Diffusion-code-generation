def list_element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and 0 <= index < len(result):
                return result[index]
            else:
                raise ValueError("Invalid index or function did not return a list")
        return wrapper
    return decorator

@list_element_retriever(3)
def fetch_data():
    return [100, 200, 300, 400, 500]

if __name__ == '__main__':
    try:
        element = fetch_data()
        print(element)
    except ValueError as e:
        print(e)