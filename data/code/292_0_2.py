import math
def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    length_value = 10
    width_value = 5
    perimeter_result = calculate_rectangle_perimeter(length_value, width_value)
    print(perimeter_result)