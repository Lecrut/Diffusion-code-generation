def calculate_time_difference(time_offsets):
    if not time_offsets:
        return 0
    min_offset = min(time_offsets)
    max_offset = max(time_offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [5, -3, 2.5, 8, -10]
    difference = calculate_time_difference(sample_offsets)
    print(difference)