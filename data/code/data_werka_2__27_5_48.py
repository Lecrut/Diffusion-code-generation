def check_not_equal(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

@check_not_equal(0)
def difference(a, b):
    return a - b

class DifferenceCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @check_not_equal(threshold=0)
    def calculate_difference(self):
        return self.a - self.b
if __name__ == '__main__':
    try:
        print(difference(9, 4))
        print(DifferenceCalculator(12, 6).calculate_difference())
        print(difference(3, 3))
    except ValueError as e:
        print(e)