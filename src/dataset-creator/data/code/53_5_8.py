def count_elements_from_start(data_list):
    if not isinstance(data_list, list) or data_list is None:
        return 0
    return len(data_list)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result_count = count_elements_from_start(sample_data)
    print(f"Total elements counted: {result_count}")