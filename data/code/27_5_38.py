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
    def __init__(self, threshold):
        self.threshold = threshold
    
    @check_not_equal(threshold=0)
    def calculate_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    try:
        calculator = DifferenceCalculator(0)
        print(calculator.calculate_difference(15, 10))
        print(calculator.calculate_difference(9, 9))
    except ValueError as e:
        print(e)

    try:
        print(difference(20, 10))
        print(difference(14, 14))
    except ValueError as e:
        print(e)