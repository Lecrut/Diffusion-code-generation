def get_first_item(array):
    if not array:
        return None
    return array[0]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = []
    sample_list_3 = ["a", "b", "c"]
    print(get_first_item(sample_list_1))
    print(get_first_item(sample_list_2))
    print(get_first_item(sample_list_3))