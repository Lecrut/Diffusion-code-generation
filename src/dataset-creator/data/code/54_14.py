def find_middle_position(data):
    if not isinstance(data, list) or len(data) < 1:
        raise ValueError("Input must be a non-empty list.")
    middle_index = (len(data)) // 2
    return data[middle_index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        result = find_middle_position(sample_list)
        print(f"Middle element is {result}")
    except ValueError as e:
        print(f"Error: {e}")