import math
def calculate_regular_polygon_area(side_lengths):
    if not side_lengths:
        return 0.0
    s = side_lengths[0]
    n = len(side_lengths)                                                     
    if len(side_lengths) == 0:
        return 0.0
    avg_s = sum(side_lengths) / len(side_lengths)
    n = len(side_lengths)
    if n < 3:
        return 0.0
    area = (n * avg_s**2) / (4 * math.tan(math.pi / n))
    return area
if __name__ == '__main__':
    list1 = [5.0, 5.0, 5.0]
    list2 = [10.0, 10.0]
    list3 = [7.0, 8.0, 9.0]
    area1 = calculate_regular_polygon_area(list1)
    area2 = calculate_regular_polygon_area(list2)
    area3 = calculate_regular_polygon_area(list3)
    print(f"Area for list1: {area1}")
    print(f"Area for list2: {area2}")
    print(f"Area for list3: {area3}")
    if area1 > area2 and area1 > area3:
        print("List 1 yields the largest area.")
    elif area2 > area1 and area2 > area3:
        print("List 2 yields the largest area.")
    else:
        print("Areas are comparable.")