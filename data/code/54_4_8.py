import math

def area_from_diameter(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = [10, 25, 50]
    for diameter in sample_diameters:
        print(f"Diameter: {diameter}, Area: {area_from_diameter(diameter)}")