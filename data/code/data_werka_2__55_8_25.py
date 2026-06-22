def calculate_triangle_perimeter(a, b, c):
    side_lengths = [a, b, c]
    if any(length <= 0 for length in side_lengths):
        raise ValueError("All side lengths must be positive numbers.")
    return sum(side_lengths)

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(9, 12, 15)
        print(perimeter)
    except ValueError as e:
        print(e)