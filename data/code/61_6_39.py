def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, list):
                raise ValueError("The function must return a list.")
            if index < 0 or index >= len(result):
                raise IndexError(f"Index {index} is out of range for the returned list.")
            return result[index]
        return wrapper
    return decorator

@element_retriever(1)
def get_values():
    return [100, 200, 300, 400, 500]

if __name__ == '__main__':
    print(get_values())