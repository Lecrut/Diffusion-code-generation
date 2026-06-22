def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if any(x <= 0 for x in (a, b, c)):
        return False
    triangle_inequalities = {
        "inequality1": a + b > c,
        "inequality2": a + c > b,
        "inequality3": b + c > a
    }
    return all(triangle_inequalities.values())

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 1, 2],
        [0, 1, 1],
        [-1, 1, 1],
        [5, 5, 5],
        [2, 2, 3]
    ]
    for sides in sample_values:
        print(can_form_triangle(sides))