def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

if __name__ == '__main__':
    num_sides = 6
    side_length = 4
    perimeter = calculate_perimeter(num_sides, side_length)
    print(f"Number of sides: {num_sides}")
    print(f"Side length: {side_length}")
    print(f"Perimeter: {perimeter}")