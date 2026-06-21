def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    base_value = 7
    height_value = 4
    try:
        area_result = calculate_parallelogram_area(base_value, height_value)
        print(f"The area of the parallelogram with base {base_value} and height {height_value} is: {area_result}")
    except ValueError as e:
        print(e)