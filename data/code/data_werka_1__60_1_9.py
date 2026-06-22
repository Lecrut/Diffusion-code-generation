def validate_input(data):
    if not isinstance(data, list):
        raise TypeError('Input must be a list')
    if not data:
        return False
    return True

def get_last_item(data):
    if not validate_input(data):
        return None
    return data[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    single_element_list = [100]
    print(get_last_item(sample_list))
    print(get_last_item(empty_list))
    print(get_last_item(single_element_list))