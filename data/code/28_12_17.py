def sort_two_floats(a, b):
    if a <= b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    print(sort_two_floats(3.5, 2.1))
    print(sort_two_floats(-1.0, -5.5))
    print(sort_two_floats(0.0, 0.0))
    print(sort_two_floats(100.0, 1.0))