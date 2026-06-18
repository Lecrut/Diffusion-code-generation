def get_last_item(data):
    if not isinstance(data, list) or len(data) == 0:
        return None
    last = data[-1]
    if isinstance(last, (list, tuple)):
        return get_last_item(list(last))
    return last
if __name__ == '__main__':
    sample_data_1 = [1, [2, [[3]]], 4]
    sample_data_2 = ['a', 'b']
    sample_data_3 = []
    sample_data_4 = [[[[[5]]]], 6]
    print(get_last_item(sample_data_1))
    print(get_last_item(sample_data_2))
    print(get_last_item(sample_data_3))
    print(get_last_item(sample_data_4))