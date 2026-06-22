def calculate_time_difference(offsets):
    if not offsets:
        return 0
    min_offset = min(offsets)
    max_offset = max(offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [5, -3, 2.5, 8, -7]
    difference = calculate_time_difference(sample_offsets)
    print(difference)