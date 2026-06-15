import math
def calculate_regular_polygon_area(side_lengths):
    if not side_lengths:
        return 0.0
    s = side_lengths[0]
    n = len(side_lengths)
    if n < 3:
        return 0.0
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area
if __name__ == '__main__':
    list1 = [5.0, 5.0, 5.0]
    list2 = [6.0, 6.0, 6.0]
    list3 = [4.0, 4.0, 4.0]
    area1 = calculate_regular_polygon_area(list1)
    area2 = calculate_regular_polygon_area(list2)
    area3 = calculate_regular_polygon_area(list3)
    print(f"Area for list1: {area1}")
    print(f"Area for list2: {area2}")
    print(f"Area for list3: {area3}")
    if area1 > area2:
        print("Area1 is greater than Area2")
    elif area1 < area2:
        print("Area1 is less than Area2")
    else:
        print("Area1 is equal to Area2")
    if area3 > area1:
        print("Area3 is greater than Area1")
    else:
        print("Area3 is less than or equal to Area1")