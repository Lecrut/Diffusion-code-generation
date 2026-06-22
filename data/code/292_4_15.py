def calculate_perimeter(num_sides, side_length):
    if num_sides < 3:
        raise ValueError("Number of sides must be at least 3")
    return num_sides * side_length

if __name__ == '__main__':
    sample_num_sides = 6
    sample_side_length = 4
    perimeter = calculate_perimeter(sample_num_sides, sample_side_length)
    print(f"Number of sides: {sample_num_sides}")
    print(f"Side length: {sample_side_length}")
    print(f"Perimeter: {perimeter}")