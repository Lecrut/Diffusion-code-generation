def calculate_cube_volume(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 3

if __name__ == '__main__':
    side = 5
    volume = calculate_cube_volume(side)
    print(volume)