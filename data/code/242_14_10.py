import math

def validate_side_length(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero")

def hexagon_area(side_length):
    validate_side_length(side_length)
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def pentagon_area(side_length):
    validate_side_length(side_length)
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2

if __name__ == '__main__':
    hexagon_side = 3
    pentagon_side = 4
    print(f"Hexagon area: {hexagon_area(hexagon_side)}")
    print(f"Pentagon area: {pentagon_area(pentagon_side)}")
    print(f"Absolute difference in areas: {abs(hexagon_area(hexagon_side) - pentagon_area(pentagon_side))}")