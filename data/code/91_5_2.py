def negate_decorator(negate):
    def wrapper(func):
        def inner(*args, **kwargs):
            return not func(*args, **kwargs)
        return inner
    return wrapper

if __name__ == '__main__':
    sample_value = True
    negated_value = negate_decorator(sample_value)(lambda: sample_value)()
    print(negated_value)