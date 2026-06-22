def calculate_perimeter(num_sides, side_length):
    if num_sides < 3:
        raise ValueError("Number of sides must be at least 3")
    return num_sides * side_length

if __name__ == '__main__':
    sample_sides = 6
    sample_length = 4
    perimeter = calculate_perimeter(sample_sides, sample_length)
    print(f"Number of sides: {sample_sides}")
    print(f"Side length: {sample_length}")
    print(f"Perimeter: {perimeter}")