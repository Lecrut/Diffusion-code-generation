def calculate_offset_difference(time_zone_offsets):
    if not time_zone_offsets:
        return 0
    min_offset = min(time_zone_offsets)
    max_offset = max(time_zone_offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [1.5, -2, 3.75, -4.5, 0]
    difference = calculate_offset_difference(sample_offsets)
    print(difference)