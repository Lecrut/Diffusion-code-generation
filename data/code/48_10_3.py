def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0:
            return False
    a, b, c = sides
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    print(is_valid_triangle([3, 4, 5]))
    print(is_valid_triangle([1, 2, 3]))
    print(is_valid_triangle([-1, 2, 3]))
    print(is_valid_triangle([0, 4, 5]))