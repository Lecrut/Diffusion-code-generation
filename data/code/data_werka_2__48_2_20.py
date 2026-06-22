TRIANGLE_SIDES_COUNT = 3

def can_form_triangle(sides):
    if len(sides) != TRIANGLE_SIDES_COUNT:
        return False
    sides.sort()
    a, b, c = sides
    return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [7, 10, 5],
        [6, 6, 6]
    ]
    for sides in sample_values:
        print(can_form_triangle(sides))