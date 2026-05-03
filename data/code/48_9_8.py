def polygon_analyzer(side_lengths, num_sides):
    if len(side_lengths) != num_sides:
        return "Error: Number of sides does not match the number of side lengths provided"
    semi_perimeter = sum(side_lengths) / 2
    return f"Polygon Type: {num_sides}-gon, Semi-perimeter: {semi_perimeter}"
if __name__ == '__main__':
    sample_sides_1 = [3, 4, 5]
    sample_sides_2 = [5, 5, 5, 5]
    sample_sides_3 = [7, 8, 9, 10]
    num_sides_1 = 3
    num_sides_2 = 4
    num_sides_3 = 4
    print(polygon_analyzer(sample_sides_1, num_sides_1))
    print(polygon_analyzer(sample_sides_2, num_sides_2))
    print(polygon_analyzer(sample_sides_3, num_sides_3))