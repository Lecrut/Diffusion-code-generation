import math

def validate_side_length(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def hexagon_area(side_length):
    validate_side_length(side_length)
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def pentagon_area(side_length):
    validate_side_length(side_length)
    return (1/4) * math.sqrt(5*(5+2*math.sqrt(5))) * side_length ** 2

if __name__ == '__main__':
    hexagon_side = 5
    pentagon_side = 3
    
    area_hexagon = hexagon_area(hexagon_side)
    area_pentagon = pentagon_area(pentagon_side)
    
    print(f"Area of Hexagon: {area_hexagon}")
    print(f"Area of Pentagon: {area_pentagon}")
    print(f"Absolute Difference in Areas: {abs(area_hexagon - area_pentagon)}")