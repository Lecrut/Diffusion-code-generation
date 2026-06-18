def find_middle_index(data):
    if not data:
        return None
    length = len(data)
    if length % 2 == 1:
        middle_index = length // 2
        return middle_index
    else:
        left_half_length = (length - 1) // 2 + 1
        right_half_start = left_half_length
        middle_indices = [right_half_start, right_half_start + 1]
        return middle_indices
if __name__ == '__main__':
    sample_list_1 = [0, 1, 2, 3, 4]
    sample_list_2 = [0, 1, 2, 3]
    result_odd = find_middle_index(sample_list_1)
    print(f"Middle index of {sample_list_1}: {result_odd}")
    result_even = find_middle_index(sample_list_2)
    print(f"Middle indices of {sample_list_2}: {result_even}")
    empty_result = find_middle_index([])
    print(f"Result for empty list: {empty_result}")