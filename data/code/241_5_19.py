def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    dimensions = {
        'sample1': (5, 10),
        'sample2': (3, 7),
        'sample3': (12, 2),
        'sample4': (4, 8)
    }
    
    areas = {key: calculate_area(*values) for key, values in dimensions.items()}
    print("Areas:")
    for key, area in areas.items():
        print(f"{key}: {area}")