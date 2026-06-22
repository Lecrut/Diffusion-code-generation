class MatchChecker:
    def __init__(self, expected_value):
        self.expected_value = expected_value

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == self.expected_value:
                return result
            else:
                raise ValueError(f"Result {result} does not match the expected value {self.expected_value}")
        return wrapper

@MatchChecker(expected_value=25)
def square(a):
    return a * a

if __name__ == '__main__':
    try:
        print(square(5))
    except ValueError as e:
        print(e)