class ThresholdChecker:

    def __init__(self, threshold):
        self.threshold = threshold

    @staticmethod
    def check_result(result, threshold):
        if result == threshold:
            raise ValueError(f'Result is equal to the threshold value: {threshold}')
        return result

    def decorated_difference(self, func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return ThresholdChecker.check_result(result, self.threshold)
        return wrapper

def difference(a, b):
    return a - b
if __name__ == '__main__':
    threshold_value = 0
    checker = ThresholdChecker(threshold_value)
    decorated_diff = checker.decorated_difference(difference)
    try:
        print(decorated_diff(5, 3))
        print(decorated_diff(4, 4))
    except ValueError as e:
        print(e)