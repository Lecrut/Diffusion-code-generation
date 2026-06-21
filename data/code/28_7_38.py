def is_larger(a, b):
    comparison_map = {'greater': lambda x, y: x > y, 'less': lambda x, y: x < y, 'equal': lambda x, y: x == y}
    return comparison_map['greater'](a, b)
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(3, 7))
    print(is_larger(-1, -2))
    print(is_larger(0, 0))