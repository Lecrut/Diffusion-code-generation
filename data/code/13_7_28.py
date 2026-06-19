def calculate_offset_difference(offsets):
    if not offsets:
        return 0
    min_offset = min(offsets)
    max_offset = max(offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [3.5, -2, 0, 4.75, 1]
    difference = calculate_offset_difference(sample_offsets)
    print(difference)