def calculate_rectangle_area(length, width):
    try:
        result = float(length) * float(width)
        if result.is_integer():
            return int(result)
        return result
    except (ValueError, TypeError) as e:
        raise ValueError("Length and width must be numbers convertible to float") from e

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3.5
    area = calculate_rectangle_area(sample_length, sample_width)
    print(area)
    sample_length_int = 10
    sample_width_int = 20
    area_int = calculate_rectangle_area(sample_length_int, sample_width_int)
    print(area_int)