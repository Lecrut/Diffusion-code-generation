import math
def calculate_radius_from_circumference(circumference):
    if circumference > 0:
        radius = circumference / (2 * math.pi)
        return radius
    else:
        return 0
if __name__ == '__main__':
    sample_circumference = 31.4159
    radius = calculate_radius_from_circumference(sample_circumference)
    print(radius)