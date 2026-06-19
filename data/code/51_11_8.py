def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    print(f"Perimeter of rectangle with length {length} and width {width}: {calculate_perimeter(length, width)}")