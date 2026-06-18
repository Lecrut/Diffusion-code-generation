def get_last_item(data):
    if not isinstance(data, list) or len(data) == 0:
        return None
    last = data[-1]
    if isinstance(last, list):
        return get_last_item(last)
    return last
if __name__ == '__main__':
    sample_data_1 = [1, 2, 3]
    result_1 = get_last_item(sample_data_1)
    sample_data_2 = [[1, 2], [3]]
    result_2 = get_last_item(sample_data_2)
    print(result_1)
    print(result_2)