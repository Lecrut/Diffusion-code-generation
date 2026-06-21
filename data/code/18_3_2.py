def get_middle_element(data):
    if not data:
        return None
    return data[len(data) // 2]

if __name__ == '__main__':
    example_list = [10, 20, 30, 40, 50]
    print(get_middle_element(example_list))
    empty_list = []
    print(get_middle_element(empty_list))
    single_item = [99]
    print(get_middle_element(single_item))
    even_items = [1, 2, 3, 4]
    print(get_middle_element(even_items))