def compute_cube_volume(edge_length):
    volume_calculated = edge_length * edge_length * edge_length
    return volume_calculated

if __name__ == '__main__':
    sample_edge_length = 7
    output_volume = compute_cube_volume(sample_edge_length)
    print(output_volume)