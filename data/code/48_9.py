import math
def analyze_polygon(side_lengths, num_sides):
    if len(side_lengths) != num_sides:
        return "Error: Number of sides does not match the number of side lengths provided"
    perimeter = sum(side_lengths)
    semi_perimeter = perimeter / 2.0
    if num_sides == 3:
        return "Triangle", semi_perimeter
    elif num_sides == 4:
        return "Quadrilateral", semi_perimeter
    elif num_sides == 5:
        return "Pentagon", semi_perimeter
    elif num_sides == 6:
        return "Hexagon", semi_perimeter
    else:
        return f"Polygon with {num_sides} sides", semi_perimeter
if __name__ == '__main__':
    sample_sides_1 = [3, 4, 5]
    sample_sides_2 = [5, 5, 5, 5]
    sample_sides_3 = [7, 8, 9, 10]
    sample_sides_4 = [10, 10, 10, 10]
    sample_sides_5 = [1, 2, 3, 4, 5]
    sample_sides_6 = [2, 3, 4, 5, 6, 7]
    num_sides_1 = 3
    num_sides_2 = 4
    num_sides_3 = 4
    num_sides_4 = 4
    num_sides_5 = 5
    num_sides_6 = 6
    print(f"Sides: {sample_sides_1}, Sides Count: {num_sides_1}")
    print(analyze_polygon(sample_sides_1, num_sides_1))
    print("-" * 20)
    print(f"Sides: {sample_sides_2}, Sides Count: {num_sides_2}")
    print(analyze_polygon(sample_sides_2, num_sides_2))
    print("-" * 20)
    print(f"Sides: {sample_sides_3}, Sides Count: {num_sides_3}")
    print(analyze_polygon(sample_sides_3, num_sides_3))
    print("-" * 20)
    print(f"Sides: {sample_sides_4}, Sides Count: {num_sides_4}")
    print(analyze_polygon(sample_sides_4, num_sides_4))
    print("-" * 20)
    print(f"Sides: {sample_sides_5}, Sides Count: {num_sides_5}")
    print(analyze_polygon(sample_sides_5, num_sides_5))
    print("-" * 20)
    print(f"Sides: {sample_sides_6}, Sides Count: {num_sides_6}")
    print(analyze_polygon(sample_sides_6, num_sides_6))
    print("-" * 20)