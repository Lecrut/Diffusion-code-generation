def sort_two_floats(a, b):
    if a <= b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    print(sort_two_floats(3.14, 2.71))
    print(sort_two_floats(-1.5, 0.0))
    print(sort_two_floats(100.0, 100.0))