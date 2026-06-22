def middle_value(data):
    n = len(data)
    if n == 0:
        raise ValueError("The list is empty")
    sorted_data = sorted(data)
    return sorted_data[n // 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Middle value for sample list:", middle_value(sample_list))
    sample_list_odd = [1, 2, 3, 4, 5]
    print("Middle value for odd length list:", middle_value(sample_list_odd))