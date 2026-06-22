def get_last_item_or_none(input_list):
    if not input_list:
        return None
    return input_list.pop()

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    result_1 = get_last_item_or_none(sample_list_1)
    print(result_1)

    sample_list_2 = []
    result_2 = get_last_item_or_none(sample_list_2)
    print(result_2)

    sample_list_3 = ['apple', 'banana', 'cherry']
    result_3 = get_last_item_or_none(sample_list_3)
    print(result_3)