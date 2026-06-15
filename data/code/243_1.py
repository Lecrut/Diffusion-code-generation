import math
def calculate_circumference(diameter):
    circumference = 2 * math.pi * diameter
    return circumference
if __name__ == '__main__':
    sample_diameter = 10
    result = calculate_circumference(sample_diameter)
    print(result)