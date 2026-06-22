import math

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    r = 5.0
    circumference = calculate_circle_circumference(r)
    print(f"Circumference: {circumference}")