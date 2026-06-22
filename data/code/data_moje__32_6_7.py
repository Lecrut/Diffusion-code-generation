def validate_dimensions(dimensions):
    width, height = dimensions
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return width, height

def calculate_rectangle_area(width, height):
    validated_width, validated_height = validate_dimensions((width, height))
    return validated_width * validated_height

if __name__ == '__main__':
    sample_width = 7
    sample_height = 3
    result = calculate_rectangle_area(sample_width, sample_height)
    print(result)