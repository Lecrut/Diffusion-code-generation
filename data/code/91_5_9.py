def negate_decorator(boolean_value):

    def wrapper():
        return not boolean_value
    return wrapper
if __name__ == '__main__':
    negated_function = negate_decorator(True)
    print(negated_function())