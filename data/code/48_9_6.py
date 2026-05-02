import math
def analyze_polygon(side_lengths, num_sides):
    if len(side_lengths) != num_sides:
        return "Error: Number of sides does not match the number of lengths provided"
    perimeter = sum(side_lengths)
    semi_perimeter = perimeter / 2
    polygon_type = ""
    if num_sides == 3:
        polygon_type = "Triangle"
    elif num_sides == 4:
        polygon_type = "Quadrilateral"
    elif num_sides == 5:
        polygon_type = "Pentagon"
    elif num_sides == 6:
        polygon_type = "Hexagon"
    else:
        polygon_type = f"{num_sides}-gon"
    return {
        "type": polygon_type,
        "semi_perimeter": semi_perimeter
    }
if __name__ == '__main__':
    sample1_sides = [3, 4, 5]
    sample1_sides_count = 3
    result1 = analyze_polygon(sample1_sides, sample1_sides_count)
    print(f"Sides: {sample1_sides}, Sides Count: {sample1_sides_count}")
    print(f"Result: {result1}")
    print("-" * 20)
    sample2_sides = [5, 5, 5, 5]
    sample2_sides_count = 4
    result2 = analyze_polygon(sample2_sides, sample2_sides_count)
    print(f"Sides: {sample2_sides}, Sides Count: {sample2_sides_count}")
    print(f"Result: {result2}")
    print("-" * 20)
    sample3_sides = [10, 10, 10]
    sample3_sides_count = 3
    result3 = analyze_polygon(sample3_sides, sample3_sides_count)
    print(f"Sides: {sample3_sides}, Sides Count: {sample3_sides_count}")
    print(f"Result: {result3}")
    print("-" * 20)
    sample4_sides = [1, 1, 1, 1]
    sample4_sides_count = 5
    result4 = analyze_polygon(sample4_sides, sample4_sides_count)
    print(f"Sides: {sample4_sides}, Sides Count: {sample4_sides_count}")
    print(f"Result: {result4}")
    print("-" * 20)