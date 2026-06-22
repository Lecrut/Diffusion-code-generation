def validate_dimensions(dimensions):
    if len(dimensions) != 2:
        raise ValueError("Dimensions must contain exactly two elements: base and height.")
    base, height = dimensions
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_area_parallelogram(dimensions):
    validate_dimensions(dimensions)
    base, height = dimensions
    return base * height

if __name__ == '__main__':
    shape_type = "parallelogram"
    dimensions = (10, 5)
    area = calculate_area_parallelogram(dimensions)
    print(f"Shape: {shape_type}")
    print(f"Dimensions: {dimensions}")
    print(f"Area: {area}")