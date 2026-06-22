def compute_cube_volume(side):
    return side * side * side

if __name__ == '__main__':
    reference_length = 6.0
    result = compute_cube_volume(reference_length)
    print(result)