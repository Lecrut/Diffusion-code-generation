NUM_SIDES = 5
SIDE_LENGTH = 3

def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

if __name__ == '__main__':
    perimeter = calculate_perimeter(NUM_SIDES, SIDE_LENGTH)
    print(f"Number of sides: {NUM_SIDES}")
    print(f"Side length: {SIDE_LENGTH}")
    print(f"Perimeter: {perimeter}")