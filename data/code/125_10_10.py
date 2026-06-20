from typing import Union

class SimpleArithmetic:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        return a * b
    
    def divide(self, a: int, b: int) -> Union[int, float]:
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b

if __name__ == '__main__':
    calculator = SimpleArithmetic()
    print(calculator.add(5, 3))
    print(calculator.subtract(10, 4))
    print(calculator.multiply(7, 2))
    try:
        print(calculator.divide(9, 0))
    except ValueError as e:
        print(e)