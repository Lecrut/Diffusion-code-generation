import math

def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = {
        "small_square": 9.0,
        "medium_square": 64.0,
        "large_square": 144.0
    }
    
    for name, area in sample_areas.items():
        side_length = find_side_length(area)
        print(f"The side length of the {name} is {side_length}")