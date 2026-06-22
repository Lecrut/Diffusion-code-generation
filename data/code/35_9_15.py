POWER_OF_VOLUME = 3

def calculate_cube_volume(edge_length):
    return edge_length ** POWER_OF_VOLUME

if __name__ == '__main__':
    side = 7
    result = calculate_cube_volume(side)
    print(result)