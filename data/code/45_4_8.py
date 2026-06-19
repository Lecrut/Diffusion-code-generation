import math
PI = math.pi

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError('Diameter must be a positive number.')
    radius = diameter / 2
    area = PI * radius ** 2
    return area

def test_calculate_circle_area():
    assert abs(calculate_circle_area(10) - PI * 25) < 1e-09, 'Test case for diameter 10 failed'
    try:
        calculate_circle_area(0)
    except ValueError as e:
        assert str(e) == 'Diameter must be a positive number.', 'Test case for diameter 0 failed'
    else:
        assert False, 'Test case for diameter 0 failed'
    try:
        calculate_circle_area(-5)
    except ValueError as e:
        assert str(e) == 'Diameter must be a positive number.', 'Test case for negative diameter failed'
    else:
        assert False, 'Test case for negative diameter failed'
if __name__ == '__main__':
    diameters = [10, 5, 2]
    for diameter in diameters:
        try:
            area = calculate_circle_area(diameter)
            print(f'The area of a circle with diameter {diameter} is: {area}')
        except ValueError as e:
            print(f'Error: {e}')
    test_calculate_circle_area()
    print('All tests passed.')