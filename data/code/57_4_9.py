def calculate_area_parallelogram(base, height):
    return base * height

if __name__ == '__main__':
    shape_type = "parallelogram"
    dimensions = {"base": 10, "height": 5}
    area = calculate_area_parallelogram(dimensions["base"], dimensions["height"])
    print(f"Shape: {shape_type}")
    print(f"Dimensions: base={dimensions['base']}, height={dimensions['height']}")
    print(f"Area: {area}")