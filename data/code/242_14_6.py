import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def pentagon_area(side_length):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2

if __name__ == '__main__':
    hex_side_length = 3
    pent_side_length = 4
    
    hex_area = hexagon_area(hex_side_length)
    pent_area = pentagon_area(pent_side_length)
    
    print(f"Area of Hexagon: {hex_area}")
    print(f"Area of Pentagon: {pent_area}")
    print(f"Absolute Difference: {abs(hex_area - pent_area)}")