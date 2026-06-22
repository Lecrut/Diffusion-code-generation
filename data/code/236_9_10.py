def replicate_line_segment(coordinates, times):
    return coordinates * times

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 1)]
    times_to_replicate = 3
    replicated_segment = replicate_line_segment(sample_coordinates, times_to_replicate)
    print(replicated_segment)