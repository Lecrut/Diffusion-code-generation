def count_elements_from_start(data_list):
    try:
        return len(data_list)
    except TypeError:
        raise ValueError("Input must be a list.")
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    if sample_data is None:
        print("Error: Input data cannot be None.")
    else:
        count_result = count_elements_from_start(sample_data)
        print(f"Total elements counted from start: {count_result}")