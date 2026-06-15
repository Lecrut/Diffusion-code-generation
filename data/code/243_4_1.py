import math
def calculate_circumference(radius):
    circumference = 2 * (radius ** 1) * math.pi
    return circumference
if __name__ == '__main__':
    sample_radius = 5
    result = calculate_circumference(sample_radius)
    print(result)