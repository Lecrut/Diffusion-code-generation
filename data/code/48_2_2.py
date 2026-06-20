def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    print(can_form_triangle([3, 4, 5]))
    print(can_form_triangle([1, 2, 3]))
    print(can_form_triangle([7, 10, 5]))
    print(can_form_triangle([0, 4, 5]))
    print(can_form_triangle([3, 4]))
    print(can_form_triangle([3, 4, 5, 6]))