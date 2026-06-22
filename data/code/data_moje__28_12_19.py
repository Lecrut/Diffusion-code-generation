def sort_two_floats(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    result = sort_two_floats(3.14, 2.71)
    print(result)
    result = sort_two_floats(10.5, 10.5)
    print(result)
    result = sort_two_floats(-5.2, -10.0)
    print(result)