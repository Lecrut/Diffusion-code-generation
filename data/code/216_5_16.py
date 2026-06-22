def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid_index = n // 2
    return sorted_data[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Middle value for sample list:", find_middle_value(sample_list))
    sample_list_odd = [10, 20, 30, 40, 50]
    print("Middle value for odd length list:", find_middle_value(sample_list_odd))
    large_list = list(range(1000000))
    print("Middle value for large list:", find_middle_value(large_list))