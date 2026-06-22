class NegativeResultException(Exception):

    def __init__(self, message):
        super().__init__(message)

def check_negative_result(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeResultException(f'Negative result detected: {result}')
        return result
    return wrapper

@check_negative_result
def compute_sum(a, b):
    return a + b

class Calculator:

    def __init__(self, initial_value=0):
        self.value = initial_value

    @check_negative_result
    def add(self, x):
        self.value += x
        return self.value

    @check_negative_result
    def subtract(self, x):
        self.value -= x
        return self.value
if __name__ == '__main__':
    try:
        print(compute_sum(5, 3))
        calc = Calculator()
        print(calc.add(10))
        print(calc.subtract(4))
        print(calc.subtract(20))
    except NegativeResultException as e:
        print(e)