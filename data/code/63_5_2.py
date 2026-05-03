def get_first_item(data):
    return data[0]
if __name__ == '__main__':
    sample_list = [10, "hello", 3.14, True]
    first_value = get_first_item(sample_list)
    print(first_value)
    sample_list_2 = ["apple", 123, None]
    first_value_2 = get_first_item(sample_list_2)
    print(first_value_2)
    sample_list_3 = ["single"]
    first_value_3 = get_first_item(sample_list_3)
    print(first_value_3)