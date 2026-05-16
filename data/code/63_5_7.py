def get_first_item(data_list):
    return data_list[0]
if __name__ == '__main__':
    sample_list_1 = [10, "hello", 3.14]
    result_1 = get_first_item(sample_list_1)
    print(result_1)
    sample_list_2 = ["apple"]
    result_2 = get_first_item(sample_list_2)
    print(result_2)
    sample_list_3 = [True]
    result_3 = get_first_item(sample_list_3)
    print(result_3)
    sample_list_4 = ["first"]
    result_4 = get_first_item(sample_list_4)
    print(result_4)