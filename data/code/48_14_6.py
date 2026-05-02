def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
if __name__ == '__main__':
    print(is_valid_triangle([3, 4, 5]))
    print(is_valid_triangle([1, 2, 3]))
    print(is_valid_triangle([1, 1, 1]))
    print(is_valid_triangle([1, 2, 4]))
    print(is_valid_triangle([0, 4, 5]))
    print(is_valid_triangle([-1, 2, 3]))
    print(is_valid_triangle([5, 5, 5]))
    print(is_valid_triangle([2, 2, 0]))