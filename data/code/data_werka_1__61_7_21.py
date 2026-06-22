def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and 0 <= index < len(result):
                return result[index]
            else:
                raise IndexError("Index out of range or result is not a list")
        return wrapper
    return decorator

@element_retriever(2)
def fetch_data():
    return [100, 200, 300, 400]

if __name__ == '__main__':
    try:
        print(fetch_data())
    except IndexError as e:
        print(e)