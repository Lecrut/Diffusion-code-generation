def calculate_time_zone_difference(offsets):
    if not offsets:
        return 0
    return max(offsets) - min(offsets)
if __name__ == '__main__':
    sample_offsets_1 = [5.5, -3.0, 10.2, -1.5]
    result_1 = calculate_time_zone_difference(sample_offsets_1)
    print(result_1)
    sample_offsets_2 = [1, 2, 3, 4]
    result_2 = calculate_time_zone_difference(sample_offsets_2)
    print(result_2)
    sample_offsets_3 = [-10, -5, -15]
    result_3 = calculate_time_zone_difference(sample_offsets_3)
    print(result_3)
    sample_offsets_4 = [0]
    result_4 = calculate_time_zone_difference(sample_offsets_4)
    print(result_4)
    sample_offsets_5 = []
    result_5 = calculate_time_zone_difference(sample_offsets_5)
    print(result_5)