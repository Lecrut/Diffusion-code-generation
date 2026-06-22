import math

CIRCLE_CONSTANTS = {
    'PERIMETER': 2 * math.pi,
}

def calculate_circle_circumference(radius):
    return CIRCLE_CONSTANTS['PERIMETER'] * radius

if __name__ == '__main__':
    r = 5.0
    circumference = calculate_circle_circumference(r)
    print(f"Radius: {r}")
    print(f"Circumference: {circumference}")