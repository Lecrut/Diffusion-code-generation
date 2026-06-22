UNIT_LABELS = {
    "square_meters": "m²",
    "square_feet": "ft²",
    "square_inches": "in²"
}

def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    dimensions = {
        "small": (2.5, 3.0),
        "large": (10.0, 20.0)
    }
    for key, dims in dimensions.items():
        area = calculate_rectangle_area(dims[0], dims[1])
        print(f"{key}: {area}")