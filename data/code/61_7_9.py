def element_retriever(index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and 0 <= index < len(result):
                return result[index]
            return None
        return wrapper
    return decorator

@element_retriever(1)
def get_elements():
    return [10, 20, 30]

if __name__ == '__main__':
    print(get_elements())