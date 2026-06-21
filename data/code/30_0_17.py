import math

UNIT_FACTORS = {
    "meters": 1.0,
    "centimeters": 0.01,
    "inches": 0.0254,
    "feet": 0.3048
}

def calculate_circle_area(radius, unit="meters"):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    conversion_factor = UNIT_FACTORS.get(unit, 1.0)
    base_radius = radius * conversion_factor
    return math.pi * (base_radius ** 2)

if __name__ == '__main__':
    sample_radius = 10
    unit = "meters"
    result = calculate_circle_area(sample_radius, unit)
    print(result)
    
    try:
        calculate_circle_area(-5, "meters")
    except ValueError as err:
        print(err)
    
    unit = "centimeters"
    result_cm = calculate_circle_area(sample_radius, unit)
    print(result_cm)