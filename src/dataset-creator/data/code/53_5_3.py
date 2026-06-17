def count_elements_from_start(data_list):
    try:
        return len(data_list)
    except TypeError:
        raise ValueError("Input must be a list.")
if __name__ == '__main__':
    sample_data = [10, 20, 30, None]
    result_count = count_elements_from_start(sample_data)
    if result_count is not None:
        print(f"Total elements counted from start: {result_count}")