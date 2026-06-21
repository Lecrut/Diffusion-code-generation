import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius ** 2

def test_calculate_circle_area():
    assert calculate_circle_area(0) == 0, 'Test case 1 failed'
    assert math.isclose(calculate_circle_area(1), math.pi), 'Test case 2 failed'
    expected_area = math.pi * 2.5 ** 2
    assert math.isclose(calculate_circle_area(2.5), expected_area), 'Test case 3 failed'
    expected_area = math.pi * 10 ** 2
    assert math.isclose(calculate_circle_area(10), expected_area), 'Test case 4 failed'
if __name__ == '__main__':
    test_calculate_circle_area()
    sample_radius = 5
    area = calculate_circle_area(sample_radius)
    print(f'The area of a circle with radius {sample_radius} is {area}')