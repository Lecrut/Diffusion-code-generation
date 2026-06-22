def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length1 = 8
    width1 = 5
    print(f"Perimeter of rectangle with length {length1} and width {width1}: {calculate_perimeter(length1, width1)}")
    
    length2 = 7.5
    width2 = 3.2
    print(f"Perimeter of rectangle with length {length2} and width {width2}: {calculate_perimeter(length2, width2)}")