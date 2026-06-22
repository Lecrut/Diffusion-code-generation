def compute_cube_volume(side_length):
    face_area = side_length * side_length
    total_volume = face_area * side_length
    return total_volume

if __name__ == '__main__':
    fixed_side = 3
    computed_vol = compute_cube_volume(fixed_side)
    print(computed_vol)