def replicate_line_segment(coordinates, times):
    return [coord for coord in coordinates for _ in range(times)]

if __name__ == '__main__':
    sample_coords = [(0, 0), (1, 2)]
    num_times = 3
    replicated_coords = replicate_line_segment(sample_coords, num_times)
    print(replicated_coords)