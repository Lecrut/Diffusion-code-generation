import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
if __name__ == '__main__':
    point1 = (0, 0)
    point2 = (3, 0)
    point3 = (0, 4)
    side1 = distance(point1, point2)
    side2 = distance(point2, point3)
    side3 = distance(point3, point1)
    print(f"Length of side 1: {side1}")
    print(f"Length of side 2: {side2}")
    print(f"Length of side 3: {side3}")