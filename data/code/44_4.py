def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    print(f"The perimeter is: {perimeter}")
if __name__ == '__main__':
    length = 10
    width = 5
    if length > 0 and width > 0:
        calculate_perimeter(length, width)
    else:
        print("Invalid input: Length and width must be positive numbers.")