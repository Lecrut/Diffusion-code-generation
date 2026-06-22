def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_length = 4.5
    result = calculate_cube_volume(sample_length)
    print(result)
    
    sample_length_zero = 0.0
    result_zero = calculate_cube_volume(sample_length_zero)
    print(result_zero)
    
    sample_length_negative = -2.0
    result_negative = calculate_cube_volume(sample_length_negative)
    print(result_negative)