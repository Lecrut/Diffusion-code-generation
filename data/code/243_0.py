import math
def calculate_circumference(radius):
    return 2 * math.pi * radius
if __name__ == '__main__':
    radius_value = 5.0
    circumference = calculate_circumference(radius_value)
    print(circumference)