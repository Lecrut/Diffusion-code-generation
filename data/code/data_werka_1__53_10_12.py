def calculate_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    area_value = 25.0
    side_length = calculate_side_length(area_value)
    print(f"The side length of the square with area {area_value} is: {side_length}")