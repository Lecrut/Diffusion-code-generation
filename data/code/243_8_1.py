import math
def calculate_radius(circumference):
    radius = circumference / (2 * math.pi)
    return radius
if __name__ == '__main__':
    sample_circumference = 62.831853
    radius = calculate_radius(sample_circumference)
    print(radius)