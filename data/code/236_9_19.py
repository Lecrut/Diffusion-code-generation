def replicate_line_segment(coordinates, times):
    return [coord for coord in coordinates for _ in range(times)]

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 1)]
    times = 3
    replicated_coordinates = replicate_line_segment(sample_coordinates, times)
    print(replicated_coordinates)