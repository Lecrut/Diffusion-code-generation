def calculate_area(side_length):
    if isinstance(side_length, (int, float)):
        return side_length * side_length
    else:
        raise ValueError("Input must be a number")

if __name__ == '__main__':
    area1 = calculate_area(5)
    print(f"Area of square 1: {area1}")
    area2 = calculate_area(10.5)
    print(f"Area of square 2: {area2}")