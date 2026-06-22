import math
NUM_SIDES = 4

def calculate_polygon_perimeter(side_lengths):
    if len(side_lengths) < NUM_SIDES:
        return 0
    perimeter = sum(side_lengths)
    return perimeter
if __name__ == '__main__':
    sample_sides = [3, 4, 5, 6]
    perimeter = calculate_polygon_perimeter(sample_sides)
    print(perimeter)