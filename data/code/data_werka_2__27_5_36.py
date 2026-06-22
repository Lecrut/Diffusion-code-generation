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

class DifferenceChecker:
    def __init__(self, threshold):
        self.threshold = threshold

    @check_not_equal(threshold=0)
    def check_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    try:
        print(difference(15, 10))
        print(difference(9, 9))
    except ValueError as e:
        print(e)

    checker = DifferenceChecker(threshold=0)
    try:
        print(checker.check_difference(20, 15))
        print(checker.check_difference(8, 8))
    except ValueError as e:
        print(e)