def calculate_quadrilateral_perimeter(side_lengths):
    if len(side_lengths) != 4:
        return None
    if not all(isinstance(side, (int, float)) and side > 0 for side in side_lengths):
        return None
    return sum(side_lengths)
if __name__ == '__main__':
    sample1 = [3, 4, 5, 6]
    result1 = calculate_quadrilateral_perimeter(sample1)
    print(result1)
    sample2 = [10, 20, 30, 40]
    result2 = calculate_quadrilateral_perimeter(sample2)
    print(result2)
    sample3 = [5, 5, 5]
    result3 = calculate_quadrilateral_perimeter(sample3)
    print(result3)
    sample4 = [1, 2, -3, 4]
    result4 = calculate_quadrilateral_perimeter(sample4)
    print(result4)