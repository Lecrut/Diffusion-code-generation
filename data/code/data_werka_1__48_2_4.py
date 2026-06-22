def can_form_triangle(sides):
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required to form a triangle.")
    
    a, b, c = sorted(sides)
    
    if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    
    return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [5, 5, 5],
        [10, 1, 1]
    ]
    
    for sides in sample_values:
        try:
            result = can_form_triangle(sides)
            print(result)
        except ValueError as e:
            print(e)