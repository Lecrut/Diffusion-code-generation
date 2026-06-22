def cube_volume(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length * side_length * side_length

if __name__ == '__main__':
    print(cube_volume(3))
    print(cube_volume(5.5))