def check_not_equal(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

def difference(a, b):
    return a - b

class DifferenceValidator:
    def __init__(self, threshold):
        self.threshold = threshold
    
    def validate_difference(self, func, a, b):
        result = func(a, b)
        if result == self.threshold:
            raise ValueError(f'Result is equal to the threshold value: {self.threshold}')
        return result

if __name__ == '__main__':
    validator = DifferenceValidator(threshold=0)
    
    try:
        print(validator.validate_difference(difference, 5, 3))
        print(validator.validate_difference(difference, 4, 4))
    except ValueError as e:
        print(e)