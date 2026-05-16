def calculate_offset_difference(offsets):
    if not offsets:
        return 0
    min_offset = min(offsets)
    max_offset = max(offsets)
    return max_offset - min_offset
if __name__ == '__main__':
    sample_offsets_1 = [5, -2, 10.5, 0]
    result_1 = calculate_offset_difference(sample_offsets_1)
    print(result_1)
    sample_offsets_2 = [300, 120, 480]
    result_2 = calculate_offset_difference(sample_offsets_2)
    print(result_2)
    sample_offsets_3 = [-5.5, 1.2, -10.0]
    result_3 = calculate_offset_difference(sample_offsets_3)
    print(result_3)
    sample_offsets_4 = [7, 7, 7]
    result_4 = calculate_offset_difference(sample_offsets_4)
    print(result_4)
    sample_offsets_5 = []
    result_5 = calculate_offset_difference(sample_offsets_5)
    print(result_5)