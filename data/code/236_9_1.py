def replicate_line_segment(coordinates, times):
    return coordinates * times

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (1, 1)]
    replication_factor = 3
    replicated_line = replicate_line_segment(sample_coordinates, replication_factor)
    print(replicated_line)