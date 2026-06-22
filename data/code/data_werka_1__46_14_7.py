def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError('Side lengths must be positive numbers.')
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        raise ValueError('The given side lengths do not form a valid triangle.')
    return sum(sides)

if __name__ == '__main__':
    try:
        side_lengths = (9, 12, 15)
        print(calculate_triangle_perimeter(*side_lengths))
        
        side_lengths = (5, 5, 8)
        print(calculate_triangle_perimeter(*side_lengths))
        
        side_lengths = (2, 3, 6)
        print(calculate_triangle_perimeter(*side_lengths))
    except ValueError as e:
        print(e)