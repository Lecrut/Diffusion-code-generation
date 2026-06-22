import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    r = 5.0
    circumference = calculate_circumference(r)
    print(f"Circumference: {circumference:.2f}")