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
    sample_data = [3, 10, -5, 22, 8, -1, 45, 0, 15]
    min_result, max_result = find_min_max_stream(sample_data)
    print(f"Minimum value: {min_result}")
    print(f"Maximum value: {max_result}")
    sample_data_2 = [1000, 500, 999, 1, 750]
    min_result_2, max_result_2 = find_min_max_stream(sample_data_2)
    print(f"Minimum value: {min_result_2}")
    print(f"Maximum value: {max_result_2}")
    sample_data_3 = []
    min_result_3, max_result_3 = find_min_max_stream(sample_data_3)
    print(f"Minimum value: {min_result_3}")
    print(f"Maximum value: {max_result_3}")