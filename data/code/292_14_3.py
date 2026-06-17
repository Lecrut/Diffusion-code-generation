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
    result1 = calculate_quadrilateral_perimeter(sample1)
    print(f"Perimeter for {sample1}: {result1}")
    sample2 = [10, 10, 10, 10]
    result2 = calculate_quadrilateral_perimeter(sample2)
    print(f"Perimeter for {sample2}: {result2}")
    sample3 = [2, 4, 6]
    result3 = calculate_quadrilateral_perimeter(sample3)
    print(f"Perimeter for {sample3}: {result3}")
    sample4 = [5, -1, 3, 4]
    result4 = calculate_quadrilateral_perimeter(sample4)
    print(f"Perimeter for {sample4}: {result4}")
    sample5 = [1, 2, 3, 4, 5]
    result5 = calculate_quadrilateral_perimeter(sample5)
    print(f"Perimeter for {sample5}: {result5}")