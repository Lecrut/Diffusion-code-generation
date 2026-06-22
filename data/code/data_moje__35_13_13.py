def calculate_cube_volume(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 3

if __name__ == '__main__':
    print(calculate_cube_volume(5))
    print(calculate_cube_volume(10.5))
    print(calculate_cube_volume(0))