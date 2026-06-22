def calculate_time_zone_difference(offsets):
    if not offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    def find_extremes(values):
        return min(values), max(values)
    
    min_offset, max_offset = find_extremes(offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [1.5, -4, 6, -2, 3]
    difference = calculate_time_zone_difference(sample_offsets)
    print(difference)