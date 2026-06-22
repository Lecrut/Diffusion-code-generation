import math

def calculate_area():
    semicircle_radius = 4
    rectangle_length = 5
    rectangle_width = 8
    
    semicircle_area = 0.5 * math.pi * (semicircle_radius ** 2)
    rectangle_area = rectangle_length * rectangle_width
    
    total_area = semicircle_area + rectangle_area
    return total_area

if __name__ == '__main__':
    print(calculate_area())