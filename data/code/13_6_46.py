def calculate_time_zone_difference(offsets):
    if not offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    min_offset = min(offsets)
    max_offset = max(offsets)
    
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [0, 5.5, -8, 3, 12]
    difference = calculate_time_zone_difference(sample_offsets)
    print(difference)