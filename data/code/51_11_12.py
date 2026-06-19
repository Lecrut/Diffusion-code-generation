def calculate_perimeter(length, width):
    if not all(isinstance(x, (int, float)) for x in [length, width]):
        raise ValueError("Length and width must be numeric.")
    return 2 * (length + width)

if __name__ == '__main__':
    length1, width1 = 3, 4
    print(f"Perimeter of rectangle with length {length1} and width {width1}: {calculate_perimeter(length1, width1)}")
    
    length2, width2 = 5.5, 2.3
    print(f"Perimeter of rectangle with length {length2} and width {width2}: {calculate_perimeter(length2, width2)}")