def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

if __name__ == '__main__':
    sides = 8
    length = 5
    perimeter = calculate_perimeter(sides, length)
    print(f"Number of sides: {sides}")
    print(f"Side length: {length}")
    print(f"Perimeter: {perimeter}")