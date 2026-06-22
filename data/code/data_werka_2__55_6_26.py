def calculate_triangle_perimeter(a, b, c):
    side_lengths = [a, b, c]
    for index, length in enumerate(side_lengths):
        if length <= 0:
            raise ValueError(f"Side {index + 1} must be a positive number")
    return sum(side_lengths)

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(9, 40, 41)
        print(perimeter)
    except ValueError as e:
        print(e)