def validate_sides(sides):
    if not isinstance(sides, list) or len(sides) != 3:
        raise ValueError("Input must be a list of exactly three side lengths.")
    for side in sides:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("All side lengths must be positive numbers.")

def can_form_triangle(sides):
    validate_sides(sides)
    a, b, c = sorted(sides)
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
            print(can_form_triangle(sides))
        except ValueError as e:
            print(e)