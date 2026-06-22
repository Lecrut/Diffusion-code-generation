TRIANGLE_SIDES_COUNT = 3

def can_form_triangle(sides):
    if len(sides) != TRIANGLE_SIDES_COUNT:
        return False
    for side in sides:
        if side <= 0:
            return False
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 1, 2],
        [0, 1, 1],
        [-1, 1, 1],
        [5, 5, 5],
        [2, 2, 3],
        [7, 10, 5],
        [6, 6, 6],
        [8, 15, 17],
        [1, 1, 2],
        [0, 5, 5],
        [-3, 4, 5]
    ]
    for sides in sample_values:
        print(can_form_triangle(sides))