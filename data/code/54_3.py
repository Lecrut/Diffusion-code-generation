import math
def get_area(radius):
    return math.pi * (radius ** 2)
if __name__ == '__main__':
    radius1 = 5.0
    area1 = get_area(radius1)
    print(f"The area for radius {radius1} is {area1}")
    radius2 = 0.5
    area2 = get_area(radius2)
    print(f"The area for radius {radius2} is {area2}")
    radius3 = 10.5
    area3 = get_area(radius3)
    print(f"The area for radius {radius3} is {area3}")