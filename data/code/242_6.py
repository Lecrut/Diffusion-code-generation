import math
def calculate_regular_polygon_area(side_lengths):
    if not side_lengths:
        return 0.0
    n = len(side_lengths)
    if n < 3:
        return 0.0
    s = side_lengths[0]
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area
if __name__ == '__main__':
    list1 = [5.0, 5.0, 5.0]
    list2 = [10.0, 10.0, 10.0]
    list3 = [7.0, 7.0, 7.0]
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
    if area2 > area3:
        print("Area2 is greater than Area3")
    elif area2 < area3:
        print("Area2 is less than Area3")
    else:
        print("Area2 is equal to Area3")