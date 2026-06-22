def is_sorted_ascending(data_list):
    for i in range(len(data_list) - 1):
        if data_list[i] > data_list[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_data = [3, 5, 8, 9, 12]
    result = is_sorted_ascending(sample_data)
    print(f"Data: {sample_data}")
    print(f"Is Sorted in Ascending Order: {result}")