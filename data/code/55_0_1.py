import sys
def calculate_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    try:
        perimeter = calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError:
        print("Error: Invalid input. Please ensure all side lengths are numbers.")