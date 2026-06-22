DIMENSION = 3

def get_cube_volume(edge_length: float) -> float:
    return edge_length ** DIMENSION

if __name__ == '__main__':
    edge_value = 4
    computed_volume = get_cube_volume(edge_value)
    print(computed_volume)