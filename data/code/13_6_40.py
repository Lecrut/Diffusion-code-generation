def calculate_time_zone_difference(offsets):
    if not offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    def find_extremes(values):
        min_value = float('inf')
        max_value = float('-inf')
        for value in values:
            if value < min_value:
                min_value = value
            if value > max_value:
                max_value = value
        return min_value, max_value
    
    min_offset, max_offset = find_extremes(offsets)
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [4, -1.5, 6, 0, -9]
    difference = calculate_time_zone_difference(sample_offsets)
    print(difference)