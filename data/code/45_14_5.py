import math

def compute_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'radius': 7}
    area = compute_area(sample_values['radius'])
    print(area)