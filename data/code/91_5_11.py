def negate_decorator(negate):
    def wrapper(func):
        if not isinstance(negate, bool):
            raise ValueError("The 'negate' parameter must be a boolean.")
        return lambda *args, **kwargs: not func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    sample_value = True
    negated_value = negate_decorator(sample_value)(lambda: sample_value)()
    print(negated_value)