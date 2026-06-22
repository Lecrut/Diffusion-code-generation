import math

def calculate_area():
    semicircle_radius = 4
    rectangle_width = 5
    rectangle_height = 8
    
    semicircle_area = 0.5 * math.pi * (semicircle_radius ** 2)
    rectangle_area = rectangle_width * rectangle_height
    
    total_area = semicircle_area + rectangle_area
    return total_area

if __name__ == '__main__':
    result = calculate_area()
    print(result)