def is_triangle(sidea, sideb, sidec):
    if sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea:
        return True
    else:
        return False
if __name__ == '__main__':
    print(is_triangle(3, 4, 5))
    print(is_triangle(1, 2, 3))
    print(is_triangle(1, 1, 1))
    print(is_triangle(1, 2, 4))
    print(is_triangle(5, 5, 5))