from math import isclose

def triangle_area(base, height):
    return lambda b, h: 0.5 * b * h

if __name__ == '__main__':
    result = triangle_area(10, 5)
    print(result(10, 5))
    assert isclose(result(10, 5), 25.0) is True