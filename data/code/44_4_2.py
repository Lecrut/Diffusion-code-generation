import sys
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    print(f"The perimeter is: {perimeter}")
if __name__ == '__main__':
    length = 10
    width = 5
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        print("Error: Length and width must be numerical.")
    else:
        calculate_perimeter(length, width)