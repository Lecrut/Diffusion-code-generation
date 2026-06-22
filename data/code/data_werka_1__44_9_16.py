def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 15
        width = 8
        perimeter = calculate_perimeter(length, width)
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)