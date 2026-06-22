def calculate_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    side1 = 5
    area1 = calculate_area(side1)
    print(f"Area of square with side length {side1}: {area1}")

    side2 = 10.5
    area2 = calculate_area(side2)
    print(f"Area of square with side length {side2}: {area2}")