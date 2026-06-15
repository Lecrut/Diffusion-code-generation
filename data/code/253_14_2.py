def find_middle_element(data):
    if len(data) != 3:
        raise ValueError("Input list must contain exactly three elements.")
    return data[1]
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        middle_value = find_middle_element(sample_list)
        print(middle_value)
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_short = [1, 2]
    try:
        find_middle_element(sample_list_short)
    except ValueError as e:
        print(f"Error for short list: {e}")
    sample_list_long = [1, 2, 3, 4]
    try:
        find_middle_element(sample_list_long)
    except ValueError as e:
        print(f"Error for long list: {e}")