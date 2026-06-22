def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    middle_index = (n - 1) // 2
    return sorted_data[middle_index]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Middle value for sample list:", find_middle_value(sample_list))
    sample_list_odd = [7, 8, 5, 2, 0, 9, 1]
    print("Middle value for odd length list:", find_middle_value(sample_list_odd))