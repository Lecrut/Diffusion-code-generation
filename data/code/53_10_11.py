def calculate_side_length(area):
    side_length = area ** 0.5
    return side_length

if __name__ == '__main__':
    hardcoded_area1 = 25.0
    side_length1 = calculate_side_length(hardcoded_area1)
    print(f"The side length of the square with area {hardcoded_area1} is: {side_length1}")

    hardcoded_area2 = 36.0
    side_length2 = calculate_side_length(hardcoded_area2)
    print(f"The side length of the square with area {hardcoded_area2} is: {side_length2}")