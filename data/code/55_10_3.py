import sys
def calculate_perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c
if __name__ == '__main__':
    side_a = 5.0
    side_b = 12.0
    side_c = 13.0
    try:
        perimeter = calculate_perimeter(side_a, side_b, side_c)
        print(f"The lengths of the sides are: {side_a}, {side_b}, and {side_c}")
        print(f"The perimeter of the triangle is: {perimeter}")
    except TypeError:
        print("Error: One or more inputs were not valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")