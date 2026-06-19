def locate_final_item_index(data):
    if not data:
        return -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == data[-1]:
            return i
    return -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    final_index = locate_final_item_index(sample_data)
    print(final_index)
    sample_data_empty = []
    final_index_empty = locate_final_item_index(sample_data_empty)
    print(final_index_empty)
    sample_data_single = [99]
    final_index_single = locate_final_item_index(sample_data_single)
    print(final_index_single)
    sample_data_repeated = [10, 20, 30, 40, 50, 30]
    final_index_repeated = locate_final_item_index(sample_data_repeated)
    print(final_index_repeated)