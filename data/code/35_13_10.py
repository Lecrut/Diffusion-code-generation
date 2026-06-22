def cube_volume(side_length):
    squared = side_length * side_length
    volume = squared * side_length
    return volume

if __name__ == '__main__':
    sample_side = 4.0
    result = cube_volume(sample_side)
    print(result)