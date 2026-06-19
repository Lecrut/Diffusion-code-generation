def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError('Side lengths must be positive numbers.')
    
    sides = sorted([a, b, c])
    smallest_side = sides[0]
    middle_side = sides[1]
    largest_side = sides[2]
    
    if smallest_side + middle_side <= largest_side:
        raise ValueError('The given side lengths do not form a valid triangle.')
    
    perimeter = smallest_side + middle_side + largest_side
    return perimeter

if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(6, 8, 10))
        print(calculate_triangle_perimeter(7, 24, 25))
        print(calculate_triangle_perimeter(2, 2, 4))
    except ValueError as e:
        print(e)