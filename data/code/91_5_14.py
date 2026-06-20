def negate_decorator(negate):
    def wrapper(func):
        def inner(*args, **kwargs):
            return not func(*args, **kwargs)
        return inner
    return wrapper

class Negator:
    def __init__(self, negate):
        self.negate = negate

    @negate_decorator(True)
    def is_even(self, number):
        return number % 2 == 0

if __name__ == '__main__':
    negator_instance = Negator(True)
    print(negator_instance.is_even(4))
    print(negator_instance.is_even(5))