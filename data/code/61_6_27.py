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
def fetch_elements():
    return ['zero', 'one', 'two', 'three', 'four', 'five']

if __name__ == '__main__':
    print(fetch_elements())