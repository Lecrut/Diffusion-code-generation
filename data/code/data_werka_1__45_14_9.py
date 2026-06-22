import math

def calculate_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'radius': 3}
    area = calculate_area(sample_values['radius'])
    print(area)