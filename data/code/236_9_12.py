def validate_coordinates(coordinates):
    if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
        raise ValueError("All elements must be tuples of two integers")

def replicate_line_segment(coordinates, times):
    validate_coordinates(coordinates)
    return [coord for _ in range(times) for coord in coordinates]

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 1)]
    replication_factor = 3
    replicated_line = replicate_line_segment(sample_coordinates, replication_factor)
    print(replicated_line)