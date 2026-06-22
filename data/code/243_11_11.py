import math

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    r = 7.5
    circumference = calculate_circle_circumference(r)
    print(f"Circumference of a circle with radius {r}: {circumference}")