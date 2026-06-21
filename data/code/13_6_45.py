def calculate_time_difference(time_offsets):
    if not time_offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    
    min_offset = min(time_offsets)
    max_offset = max(time_offsets)
    
    return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = [2.5, -3.0, 1.0, 4.5, -1.5]
    difference = calculate_time_difference(sample_offsets)
    print(difference)