def calculate_time_difference(offsets):
    if not offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    min_offset = min(offsets)
    max_offset = max(offsets)
    
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [5.5, -3.0, 2.0, 8.0, -1.5]
    difference = calculate_time_difference(sample_offsets)
    print(difference)