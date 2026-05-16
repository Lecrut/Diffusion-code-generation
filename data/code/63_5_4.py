def get_first_item(data_list):
    return data_list[0]
if __name__ == '__main__':
    sample_list = [10, "hello", 3.14, True]
    first_item = get_first_item(sample_list)
    print(first_item)
    sample_list_2 = ["apple", 100, None]
    first_item_2 = get_first_item(sample_list_2)
    print(first_item_2)