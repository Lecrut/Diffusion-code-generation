def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    perimeter_result = calculate_perimeter(length, width)
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Perimeter: {perimeter_result}")