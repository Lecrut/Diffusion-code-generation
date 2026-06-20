def negate_decorator(boolean):
    def wrapper():
        return not boolean
    return wrapper

if __name__ == '__main__':
    sample_boolean = True
    negated_function = negate_decorator(sample_boolean)
    print(negated_function())