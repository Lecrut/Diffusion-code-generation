def calculate_time_zone_difference(offsets):
    if not offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    min_offset = min(offsets)
    max_offset = max(offsets)
    
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [5.5, 7.0, -3.0, 2.0, 8.0]
    difference = calculate_time_zone_difference(sample_offsets)
    print(difference)