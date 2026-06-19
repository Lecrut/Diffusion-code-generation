def get_last_item(data):
    return data[-1] if data else None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    single_element_list = [77]
    print(get_last_item(sample_list))
    print(get_last_item(empty_list))
    print(get_last_item(single_element_list))