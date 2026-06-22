def is_sorted_ascending(data_list):
    if not data_list:
        return True
    for i in range(1, len(data_list)):
        if data_list[i] < data_list[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data}")
    print(f"Is Sorted in Ascending Order: {is_sorted_ascending(sample_data)}")
    
    sample_data_desc = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Data: {sample_data_desc}")
    print(f"Is Sorted in Ascending Order: {is_sorted_ascending(sample_data_desc)}")
    
    sample_data_empty = []
    print(f"Data: {sample_data_empty}")
    print(f"Is Sorted in Ascending Order: {is_sorted_ascending(sample_data_empty)}")