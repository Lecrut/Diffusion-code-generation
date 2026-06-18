def count_elements_from_start(data_list):
    try:
        return len(data_list)
    except TypeError:
        raise ValueError("Input must be a list.")
if __name__ == '__main__':
    sample_data = [10, 20, 30, None]
    if not isinstance(sample_data, list):
        print("Error: Input is not a valid list.")
    else:
        count_result = count_elements_from_start(sample_data)
        if count_result is not None:
            print(f"Total elements counted from start: {count_result}")