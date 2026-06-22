def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

if __name__ == '__main__':
    sample_values = {
        'num_sides': 5,
        'side_length': 3
    }
    perimeter = calculate_perimeter(**sample_values)
    print(f"Number of sides: {sample_values['num_sides']}")
    print(f"Side length: {sample_values['side_length']}")
    print(f"Perimeter: {perimeter}")