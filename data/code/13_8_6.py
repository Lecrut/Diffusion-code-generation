def calculate_time_zone_difference(offsets):
    if not offsets:
        return 0
    min_offset = min(offsets)
    max_offset = max(offsets)
    return max_offset - min_offset
if __name__ == '__main__':
    sample_offsets_1 = [5, -2, 10.5, -1]
    result_1 = calculate_time_zone_difference(sample_offsets_1)
    print(result_1)
    sample_offsets_2 = [300, 120, 240]
    result_2 = calculate_time_zone_difference(sample_offsets_2)
    print(result_2)
    sample_offsets_3 = [-5, -10, -1]
    result_3 = calculate_time_zone_difference(sample_offsets_3)
    print(result_3)
    sample_offsets_4 = []
    result_4 = calculate_time_zone_difference(sample_offsets_4)
    print(result_4)