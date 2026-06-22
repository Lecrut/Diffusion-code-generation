def calculate_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    try:
        example_area = 81
        side_length_result = calculate_side_length(example_area)
        print(f"The side length of the square with area {example_area} is: {side_length_result}")
    except ValueError as e:
        print(e)