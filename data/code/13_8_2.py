def calculate_time_zone_difference(offsets):
    if not offsets:
        return 0
    return max(offsets) - min(offsets)
if __name__ == '__main__':
    sample_offsets_1 = [5, -3, 10, -1]
    result_1 = calculate_time_zone_difference(sample_offsets_1)
    print(result_1)
    sample_offsets_2 = [1.5, 0.5, 2.0, -1.0]
    result_2 = calculate_time_zone_difference(sample_offsets_2)
    print(result_2)
    sample_offsets_3 = [10, 10, 10]
    result_3 = calculate_time_zone_difference(sample_offsets_3)
    print(result_3)
    sample_offsets_4 = []
    result_4 = calculate_time_zone_difference(sample_offsets_4)
    print(result_4)