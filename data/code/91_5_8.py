def negate_decorator(boolean):

    def wrapper():
        return not boolean
    return wrapper
if __name__ == '__main__':
    negated = negate_decorator(True)
    print(negated())