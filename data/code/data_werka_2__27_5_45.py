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
    def __init__(self, threshold=0):
        self.threshold = threshold

    @check_not_equal(threshold=0)
    def calculate(self, a, b):
        return a - b

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    try:
        print(calculator.calculate(15, 7))
        print(calculator.calculate(9, 9))
    except ValueError as e:
        print(e)