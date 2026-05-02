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
    sample_list = [10, 20, 30, 40]
    result = get_first(sample_list)
    print(result)
    sample_list_empty = []
    result_empty = get_first(sample_list_empty)
    print(result_empty)
    sample_list_single = [99]
    result_single = get_first(sample_list_single)
    print(result_single)