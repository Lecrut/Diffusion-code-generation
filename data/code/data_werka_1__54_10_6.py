import math

def area_of_circle(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'radius': 10}
    print(area_of_circle(sample_values['radius']))