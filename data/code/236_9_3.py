def replicate_line_segment(coordinates, times):
    return [coord for coord_list in [coordinates] * times for coord in coord_list]

if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4)]
    times_to_replicate = 3
    replicated_coordinates = replicate_line_segment(sample_coordinates, times_to_replicate)
    print(replicated_coordinates)