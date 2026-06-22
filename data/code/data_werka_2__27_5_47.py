THRESHOLD = 0

def check_not_equal(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

@check_not_equal(THRESHOLD)
def difference(a, b):
    return a - b

class DifferenceCalculator:

    def __init__(self, threshold=THRESHOLD):
        self.threshold = threshold

    @check_not_equal(threshold=THRESHOLD)
    def calculate_difference(self, a, b):
        return a - b
if __name__ == '__main__':
    try:
        print(difference(15, 10))
        print(DifferenceCalculator().calculate_difference(20, 5))
        print(difference(9, 9))
    except ValueError as e:
        print(e)