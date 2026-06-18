def count_elements_from_start(data_list):
    try:
        return len(data_list)
    except TypeError:
        raise ValueError("Input must be a list.")
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    if not isinstance(sample_data, list):
        print(f"Error: Input is not a valid list. Received {type(sample_data).__name__}")
    else:
        count_result = count_elements_from_start(sample_data)
        print(f"The number of elements in the sample data from start to end is: {count_result}")