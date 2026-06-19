SQUARE_ROOT = 0.5

def calculate_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** SQUARE_ROOT

if __name__ == '__main__':
    sample_areas = [25.0, 10.0, 0.0, 12.3456]
    for i, area in enumerate(sample_areas):
        side_length = calculate_side_length(area)
        print(f"Sample {i+1}: Area: {area}, Side Length: {side_length}")