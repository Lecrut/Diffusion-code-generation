def list_accessor(target_list, index_to_retrieve):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 0 <= index_to_retrieve < len(target_list):
                return target_list[index_to_retrieve]
            else:
                raise IndexError("Index out of range")
        return wrapper
    return decorator

data = [10, 20, 30, 40, 50]

@list_accessor(data, 2)
def get_element():
    return "This value is ignored"

if __name__ == '__main__':
    result = get_element()
    print(result)