def match_checker(expected_value):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return result
            else:
                raise ValueError(f'Result {result} does not match the expected value {expected_value}')
        return wrapper
    return decorator
TARGET_VALUE = 25

@match_checker(TARGET_VALUE)
def calculate_area(length, width):
    return length * width

class Geometry:

    def __init__(self):
        self.shapes = []

    @match_checker(3.14159)
    def circle_area(self, radius):
        import math
        return math.pi * radius ** 2
if __name__ == '__main__':
    try:
        print(calculate_area(5, 5))
    except ValueError as e:
        print(e)
    geo = Geometry()
    try:
        print(geo.circle_area(1))
    except ValueError as e:
        print(e)