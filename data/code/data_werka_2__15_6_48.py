CONSTANT_VALUE = 42

def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return result
            else:
                raise ValueError(f"Result {result} does not match the expected value {expected_value}")
        return wrapper
    return decorator

@match_checker(CONSTANT_VALUE)
def compute_answer():
    return 6 * 7

class Validator:
    def __init__(self, value):
        self.value = value

    @match_checker(CONSTANT_VALUE)
    def validate(self):
        return self.value

if __name__ == '__main__':
    try:
        print(compute_answer())
    except ValueError as e:
        print(e)

    validator = Validator(42)
    try:
        print(validator.validate())
    except ValueError as e:
        print(e)