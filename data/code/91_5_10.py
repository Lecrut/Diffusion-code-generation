def negate_decorator(negate):
    def wrapper(func):
        def inner(*args, **kwargs):
            return not func(*args, **kwargs)
        return inner
    return wrapper

@negate_decorator(False)
def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_value = False
    negated_value = negate_decorator(sample_value)(lambda: sample_value)()
    print(negated_value)