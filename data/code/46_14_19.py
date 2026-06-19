def calculate_triangle_perimeter(a, b, c):
    side_lengths = {'a': a, 'b': b, 'c': c}
    
    for length in side_lengths.values():
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError('Side lengths must be positive numbers.')
    
    sides = sorted(side_lengths.values())
    if sides[0] + sides[1] <= sides[2]:
        raise ValueError('The given side lengths do not form a valid triangle.')
    
    return sum(sides)

if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(6, 8, 10))
        print(calculate_triangle_perimeter(7, 24, 25))
        print(calculate_triangle_perimeter(1, 1, 2))
    except ValueError as e:
        print(e)