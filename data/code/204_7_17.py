import numpy as np
MIDDLE_INDEX = 0

def compute_middle_value(data):
    if not data:
        return None
    sorted_data = np.sort(data)
    n = len(sorted_data)
    if n % 2 == 1:
        MIDDLE_INDEX = n // 2
        return sorted_data[MIDDLE_INDEX]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (sorted_data[middle_left_index] + sorted_data[middle_right_index]) / 2
if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(compute_middle_value(sample_list1))
    sample_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(compute_middle_value(sample_list2))
    sample_list3 = []
    print(compute_middle_value(sample_list3))