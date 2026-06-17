def calculate_quadrilateral_perimeter(side_lengths):
    if len(side_lengths) != 4:
        return "Error: Input must contain exactly four side lengths."
    for side in side_lengths:
        if not isinstance(side, (int, float)) or side <= 0:
            return "Error: All side lengths must be positive numbers."
    perimeter = sum(side_lengths)
    return perimeter
if __name__ == '__main__':
    sample1 = [3, 4, 5, 6]
    print(calculate_quadrilateral_perimeter(sample1))
    sample2 = [10, 20, 30, 40]
    print(calculate_quadrilateral_perimeter(sample2))
    sample3 = [5, 5, 5]
    print(calculate_quadrilateral_perimeter(sample3))
    sample4 = [1, -2, 3, 4]
    print(calculate_quadrilateral_perimeter(sample4))
    sample5 = [1, 2, 3]
    print(calculate_quadrilateral_perimeter(sample5))