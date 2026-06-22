def check_not_equal(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

class DifferenceCalculator:
    def __init__(self, threshold=0):
        self.threshold = threshold

    @check_not_equal(threshold=0)
    def calculate_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    try:
        print(calculator.calculate_difference(15, 10))
        print(calculator.calculate_difference(20, 20))
    except ValueError as e:
        print(e)