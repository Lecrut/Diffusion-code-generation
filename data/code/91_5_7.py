def negate_decorator(negate):
    def wrapper(func):
        def inner(*args, **kwargs):
            return not func(*args, **kwargs)
        return inner
    return wrapper

class Negator:
    def __init__(self, value):
        self.value = value
    
    @negate_decorator(True)
    def get_value(self):
        return self.value

if __name__ == '__main__':
    negator_instance = Negator(True)
    print(negator_instance.get_value())
    negator_instance.value = False
    print(negator_instance.get_value())