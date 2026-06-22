def replicate_line_segment(coordinates, times):
    return [pair for pair in coordinates for _ in range(times)]

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 2)]
    times_to_replicate = 3
    replicated_coordinates = replicate_line_segment(sample_coordinates, times_to_replicate)
    print(replicated_coordinates)