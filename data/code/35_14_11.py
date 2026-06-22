import math

def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return math.pow(edge_length, 3)

if __name__ == '__main__':
    sample_edge = 5
    result = calculate_cube_volume(sample_edge)
    print(result)
    
    sample_edge_float = 2.5
    result_float = calculate_cube_volume(sample_edge_float)
    print(result_float)