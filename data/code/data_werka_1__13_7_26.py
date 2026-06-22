def calculate_time_difference(time_offsets):
    if not time_offsets:
        return 0
    min_offset = min(time_offsets)
    max_offset = max(time_offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [1.5, -2.3, 4.8, 0.0, -3.7]
    difference = calculate_time_difference(sample_offsets)
    print(difference)