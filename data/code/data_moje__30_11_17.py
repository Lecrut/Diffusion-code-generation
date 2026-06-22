import math

CIRCLE_METRICS = {
    "radius": 5,
    "formula": "pi * r**2"
}

def compute_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    current_radius = CIRCLE_METRICS["radius"]
    computed_area = compute_circle_area(current_radius)
    print(computed_area)