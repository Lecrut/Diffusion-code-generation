def cube_volume(edge_length):
    unit_mapping = {'cube': 3}
    power = unit_mapping['cube']
    return edge_length ** power

if __name__ == '__main__':
    sample_edge = 6
    computed_volume = cube_volume(sample_edge)
    print(computed_volume)