def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c
if __name__ == '__main__':
    print(can_form_triangle([3, 4, 5]))
    print(can_form_triangle([1, 2, 3]))
    print(can_form_triangle([5, 5, 5]))
    print(can_form_triangle([10, 1, 1]))