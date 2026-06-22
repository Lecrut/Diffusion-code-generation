def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

if __name__ == '__main__':
    sample_sides = 7
    sample_length = 2
    perimeter = calculate_perimeter(sample_sides, sample_length)
    print(f"Number of sides: {sample_sides}")
    print(f"Side length: {sample_length}")
    print(f"Perimeter: {perimeter}")