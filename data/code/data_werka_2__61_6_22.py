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

@element_retriever(3)
def fetch_data():
    return ['apple', 'banana', 'cherry', 'date', 'elderberry']

if __name__ == '__main__':
    print(fetch_data())