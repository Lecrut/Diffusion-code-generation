def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, list):
                raise ValueError("The function must return a list.")
            try:
                return result[index]
            except IndexError as e:
                raise IndexError(f"Index {index} is out of range for the returned list.") from e
        return wrapper
    return decorator

@element_retriever(4)
def retrieve_numbers():
    return [5, 15, 25, 35, 45, 55]

if __name__ == '__main__':
    print(retrieve_numbers())