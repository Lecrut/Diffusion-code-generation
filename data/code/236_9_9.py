def replicate_line_segment(coordinates, times):
    if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
        raise ValueError("All elements in coordinates must be tuples of length 2")
    if not isinstance(times, int) or times < 0:
        raise ValueError("Times must be a non-negative integer")
    
    return [coord for _ in range(times) for coord in coordinates]

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 1)]
    replication_factor = 3
    replicated_line = replicate_line_segment(sample_coordinates, replication_factor)
    print(replicated_line)