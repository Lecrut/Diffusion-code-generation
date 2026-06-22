TRIANGLE_SIDES_COUNT = 3

def can_form_triangle(sides):
    if len(sides) != TRIANGLE_SIDES_COUNT:
        return False
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [7, 10, 5],
        [8, 15, 17]
    ]
    for sides in sample_values:
        print(can_form_triangle(sides))