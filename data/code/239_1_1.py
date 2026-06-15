import math
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)
if __name__ == '__main__':
    length_val = 10
    width_val = 5
    perimeter = calculate_rectangle_perimeter(length_val, width_val)
    print(perimeter)