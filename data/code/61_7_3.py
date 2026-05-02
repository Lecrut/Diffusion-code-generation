def list_accessor(target_list, index_to_retrieve):
    def decorator(func):
        def wrapper(*args):
            return target_list[index_to_retrieve]
        return wrapper
    return decorator
data = [10, 20, 30, 40, 50]
@list_accessor(data, 2)
def get_third_element(x):
    return x
if __name__ == '__main__':
    result = get_third_element(1)
    print(result)