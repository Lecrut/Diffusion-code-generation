def list_accessor(target_list, index_to_retrieve):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(target_list, list):
                raise TypeError("The target must be a list")
            if not isinstance(index_to_retrieve, int):
                raise ValueError("Index must be an integer")
            if index_to_retrieve < 0 or index_to_retrieve >= len(target_list):
                raise IndexError("Index out of range")
            return func(*args, **kwargs)
        return wrapper
    return decorator

data = [10, 20, 30, 40, 50]
@list_accessor(data, 2)
def get_element(x):
    return x

if __name__ == '__main__':
    result = get_element(1)
    print(result)