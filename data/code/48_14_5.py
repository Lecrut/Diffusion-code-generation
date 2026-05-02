def is_valid_triangle(side_lengths):
    if len(side_lengths) != 3:
        return False
    a = side_lengths[0]
    b = side_lengths[1]
    c = side_lengths[2]
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
    print(is_valid_triangle([2, 2, 3]))