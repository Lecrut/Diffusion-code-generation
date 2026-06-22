def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("The output is zero.")
        else:
            print(f"The output is not zero: {result}")
        return result
    return wrapper

class Calculator:
    @check_zero_result
    def add(self, a, b):
        return a + b

    @check_zero_result
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.add(-2, 2))
    print(calc.multiply(4, 0))
    print(calc.multiply(6, 7))