def negate_decorator(negate):
    def wrapper(func):
        def inner(*args, **kwargs):
            return not func(*args, **kwargs)
        return inner
    return wrapper

@negate_decorator(True)
def is_positive(number):
    return number > 0

if __name__ == '__main__':
    sample_value = -5
    negated_result = is_positive(sample_value)
    print(negated_result)