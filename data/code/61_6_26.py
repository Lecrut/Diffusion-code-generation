def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and 0 <= index < len(result):
                return result[index]
            else:
                raise ValueError("Index out of range or invalid result type")
        return wrapper
    return decorator

@element_retriever(2)
def get_elements():
    return [10, 20, 30, 40]

if __name__ == '__main__':
    print(get_elements())