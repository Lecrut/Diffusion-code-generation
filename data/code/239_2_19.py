PERIMETER_FACTOR = 2

def calculate_rectangle_perimeter(length, width):
    return PERIMETER_FACTOR * (length + width)
if __name__ == '__main__':
    length1, width1 = (10, 5)
    length2, width2 = (7, 3)
    perimeter1 = calculate_rectangle_perimeter(length1, width1)
    perimeter2 = calculate_rectangle_perimeter(length2, width2)
    print(f'Perimeter of rectangle with length {length1} and width {width1}: {perimeter1}')
    print(f'Perimeter of rectangle with length {length2} and width {width2}: {perimeter2}')