import math
def calculate_regular_polygon_area(side_lengths):
    if not side_lengths:
        return 0.0
    n = len(side_lengths)
    if n == 0:
        return 0.0
    s = side_lengths[0]
    N = n
    if s <= 0:
        return 0.0
    area = (N * s**2) / (4 * math.tan(math.pi / N))
    return area
def compare_polygon_areas(list1, list2):
    area1 = calculate_regular_polygon_area(list1)
    area2 = calculate_regular_polygon_area(list2)
    comparison = {
        "area1": area1,
        "area2": area2,
        "difference": area1 - area2,
        "result": "Area 1 is greater" if area1 > area2 else ("Area 2 is greater" if area2 > area1 else "Areas are equal")
    }
    return comparison
if __name__ == '__main__':
    list_a = [5.0, 5.0, 5.0]
    list_b = [6.0, 6.0, 6.0]
    list_c = [10.0, 10.0]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"List C: {list_c}\n")
    comparison_ab = compare_polygon_areas(list_a, list_b)
    print("Comparison between List A and List B:")
    print(f"Area 1: {comparison_ab['area1']}")
    print(f"Area 2: {comparison_ab['area2']}")
    print(f"Difference (A - B): {comparison_ab['difference']}")
    print(f"Result: {comparison_ab['result']}\n")
    comparison_ac = compare_polygon_areas(list_a, list_c)
    print("Comparison between List A and List C:")
    print(f"Area 1: {comparison_ac['area1']}")
    print(f"Area 2: {comparison_ac['area2']}")
    print(f"Difference (A - C): {comparison_ac['difference']}")
    print(f"Result: {comparison_ac['result']}")