def get_first_element(func):
    def wrapper(*args):
        if not args:
            return None
        return args[0]
    return wrapper
@get_first_element
def get_first(data_list):
    return data_list
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result = get_first(sample_data)
    print(result)
    sample_data_2 = ['a', 'b', 'c']
    result_2 = get_first(sample_data_2)
    print(result_2)
    empty_data = []
    result_3 = get_first(empty_data)
    print(result_3)