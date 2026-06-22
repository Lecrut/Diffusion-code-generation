def cube_volume(edge):
    cubic_power = edge * edge * edge
    return cubic_power

if __name__ == '__main__':
    side_length = 7
    volume_result = cube_volume(side_length)
    print(volume_result)