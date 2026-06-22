def calculate_time_zone_difference(offsets):
    if not offsets:
        return 0
    min_offset = min(offsets)
    max_offset = max(offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [1.5, -2.0, 3.0, 0.0, -1.5]
    difference = calculate_time_zone_difference(sample_offsets)
    print(difference)