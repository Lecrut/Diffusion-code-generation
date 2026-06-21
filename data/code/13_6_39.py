def calculate_offset_difference(time_zone_offsets):
    if not time_zone_offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    min_offset = min(time_zone_offsets)
    max_offset = max(time_zone_offsets)
    
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [1.5, -2.0, 3.0, 0.0, -1.5]
    difference = calculate_offset_difference(sample_offsets)
    print(difference)