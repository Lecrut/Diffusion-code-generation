import math

CIRCLE_AREA = math.pi

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return radius * radius * CIRCLE_AREA

if __name__ == '__main__':
    test_r = 4
    computed = circle_area(test_r)
    print(computed)
    test_neg = -2
    try:
        circle_area(test_neg)
    except ValueError as e:
        print(e)