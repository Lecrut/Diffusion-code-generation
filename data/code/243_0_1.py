import math
def calculate_circumference(radius):
    return 2 * math.pi * radius
if __name__ == '__main__':
    radius = 5
    circumference = calculate_circumference(radius)
    print(circumference)