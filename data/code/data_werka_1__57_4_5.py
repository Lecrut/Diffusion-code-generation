def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    shape_type = "parallelogram"
    dimensions = {"base": 10, "height": 5}
    area = calculate_parallelogram_area(dimensions["base"], dimensions["height"])
    print(f"Shape: {shape_type}")
    print(f"Dimensions: Base={dimensions['base']}, Height={dimensions['height']}")
    print(f"Area: {area}")