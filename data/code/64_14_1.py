import numpy as np
def locate_final_item_index(data_list):
    if not data_list:
        return -1
    return len(data_list) - 1
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