import math
def analyze_polygon(side_lengths, num_sides):
    if len(side_lengths) != num_sides:
        return "Error: Number of sides does not match the list length"
    semi_perimeter = sum(side_lengths) / 2
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
    num_sides_1 = 3
    num_sides_2 = 4
    num_sides_3 = 4
    num_sides_4 = 6
    result1 = analyze_polygon(sample_sides_1, num_sides_1)
    result2 = analyze_polygon(sample_sides_2, num_sides_2)
    result3 = analyze_polygon(sample_sides_3, num_sides_3)
    result4 = analyze_polygon(sample_sides_4, num_sides_4)
    print(f"Sides: {sample_sides_1}, Sides: {num_sides_1} -> Result: {result1}")
    print(f"Sides: {sample_sides_2}, Sides: {num_sides_2} -> Result: {result2}")
    print(f"Sides: {sample_sides_3}, Sides: {num_sides_3} -> Result: {result3}")
    print(f"Sides: {sample_sides_4}, Sides: {num_sides_4} -> Result: {result4}")