def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, list):
                raise ValueError("The function must return a list.")
            try:
                return result[index]
            except IndexError:
                raise IndexError(f"Index {index} is out of range for the returned list.")
        return wrapper
    return decorator

@element_retriever(2)
def retrieve_items():
    return [100, 200, 300, 400]

if __name__ == '__main__':
    print(retrieve_items())