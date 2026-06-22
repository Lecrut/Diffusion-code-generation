def validate_inputs(num_sides, side_length):
    if not isinstance(num_sides, int) or num_sides < 3:
        raise ValueError("Number of sides must be an integer greater than or equal to 3")
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")

def calculate_perimeter(num_sides, side_length):
    validate_inputs(num_sides, side_length)
    return num_sides * side_length

if __name__ == '__main__':
    num_sides = 7
    side_length = 2.5
    perimeter = calculate_perimeter(num_sides, side_length)
    print(f"Number of sides: {num_sides}")
    print(f"Side length: {side_length}")
    print(f"Perimeter: {perimeter}")