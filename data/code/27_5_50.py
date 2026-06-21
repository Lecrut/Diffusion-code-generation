class ThresholdChecker:
    DEFAULT_THRESHOLD = 0

    @staticmethod
    def check_not_equal(threshold):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if result == threshold:
                    raise ValueError(f'Result is equal to the threshold value: {threshold}')
                return result
            return wrapper
        return decorator

@ThresholdChecker.check_not_equal(ThresholdChecker.DEFAULT_THRESHOLD)
def difference(a, b):
    return a - b

if __name__ == '__main__':
    try:
        print(difference(9, 4))
        print(difference(5, 5))
    except ValueError as e:
        print(e)