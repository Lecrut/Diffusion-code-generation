class ListAccessor:

    def __init__(self, target_list):
        self.target_list = target_list

    def decorator(self, index_to_retrieve):

        def wrapper(func):

            def inner_func(*args, **kwargs):
                if 0 <= index_to_retrieve < len(self.target_list):
                    return self.target_list[index_to_retrieve]
                else:
                    raise IndexError('Index out of range')
            return inner_func
        return wrapper
data = [10, 20, 30, 40, 50]
accessor = ListAccessor(data)

@accessor.decorator(2)
def get_element(x):
    return x
if __name__ == '__main__':
    try:
        result = get_element(1)
        print(result)
    except IndexError as e:
        print(e)

    @accessor.decorator(4)
    def get_fifth_element(y):
        return y
    try:
        result = get_fifth_element(2)
        print(result)
    except IndexError as e:
        print(e)
    try:

        @accessor.decorator(10)
        def out_of_range_element(z):
            return z
        result = out_of_range_element(3)
        print(result)
    except IndexError as e:
        print(e)