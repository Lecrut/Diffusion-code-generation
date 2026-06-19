def get_first_item(data):
    return data[0]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [42, "world", 2.718]
    SAMPLE_LIST_2 = ["banana", 99, [3, 4]]
    SINGLE_ITEM_LIST = ["unique"]

    first_value_1 = get_first_item(SAMPLE_LIST_1)
    first_value_2 = get_first_item(SAMPLE_LIST_2)
    single_value = get_first_item(SINGLE_ITEM_LIST)

    print(first_value_1)
    print(first_value_2)
    print(single_value)