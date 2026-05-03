import numpy as np
def locate_final_item_index(data):
    if not data:
        return -1
    return len(data) - 1
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = locate_final_item_index(sample_data)
    print(result)
    sample_data_empty = []
    result_empty = locate_final_item_index(sample_data_empty)
    print(result_empty)
    sample_data_single = [99]
    result_single = locate_final_item_index(sample_data_single)
    print(result_single)