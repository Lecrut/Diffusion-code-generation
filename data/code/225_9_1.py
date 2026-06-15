import math
def find_min_max_stream(data_stream):
    if not data_stream:
        return None, None
    min_val = data_stream[0]
    max_val = data_stream[0]
    for number in data_stream[1:]:
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number
    return min_val, max_val
if __name__ == '__main__':
    sample_data = [3, 10, -5, 20, 1, 15, -100, 42]
    min_result, max_result = find_min_max_stream(sample_data)
    print(f"Minimum value: {min_result}")
    print(f"Maximum value: {max_result}")
    sample_data_large = [1000, -500, 2000, -100, 3000, -750]
    min_result_large, max_result_large = find_min_max_stream(sample_data_large)
    print(f"Minimum value: {min_result_large}")
    print(f"Maximum value: {max_result_large}")
    empty_data = []
    min_result_empty, max_result_empty = find_min_max_stream(empty_data)
    print(f"Minimum value (empty): {min_result_empty}")
    print(f"Maximum value (empty): {max_result_empty}")