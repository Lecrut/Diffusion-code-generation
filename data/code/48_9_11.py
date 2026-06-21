def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    triangle_inequality_1 = (a + b > c)
    triangle_inequality_2 = (a + c > b)
    triangle_inequality_3 = (b + c > a)
    return triangle_inequality_1 and triangle_inequality_2 and triangle_inequality_3

if __name__ == '__main__':
    sample_values = [
        [7, 10, 5],
        [6, 6, 6],
        [8, 15, 17],
        [1, 1, 2],
        [0, 5, 5],
        [-3, 4, 5]
    ]
    for sides in sample_values:
        print(can_form_triangle(sides))