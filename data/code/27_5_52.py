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
    def calculate(self):
        return self.a - self.b

if __name__ == '__main__':
    try:
        print(difference(15, 7))
        print(DifferenceCalculator(9, 3).calculate())
        print(difference(2, 2))
        print(DifferenceCalculator(8, 8).calculate())
    except ValueError as e:
        print(e)