def is_sorted_ascending(data_list):
    for i in range(1, len(data_list)):
        if data_list[i] < data_list[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data}")
    print(f"Is Sorted in Ascending Order: {is_sorted_ascending(sample_data)}")