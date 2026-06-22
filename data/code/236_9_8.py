def replicate_line_segment(coordinates, times):
    return coordinates * times

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 2)]
    sample_times = 3
    replicated_segment = replicate_line_segment(sample_coordinates, sample_times)
    print(replicated_segment)