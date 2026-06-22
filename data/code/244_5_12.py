import math

def calculate_area():
    semicircle_radius = 4
    rectangle_length = 5
    rectangle_width = 8
    areas = {
        'semicircle': 0.5 * math.pi * (semicircle_radius ** 2),
        'rectangle': rectangle_length * rectangle_width
    }
    total_area = sum(areas.values())
    return total_area

if __name__ == '__main__':
    result = calculate_area()
    print(result)