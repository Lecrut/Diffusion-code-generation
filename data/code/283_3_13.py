def is_sorted_ascending(data_list):
    return all(data_list[i] <= data_list[i + 1] for i in range(len(data_list) - 1))

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data}")
    print(f"Is Sorted in Ascending Order: {is_sorted_ascending(sample_data)}")