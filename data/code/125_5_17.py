from typing import Union

class BasicArithmetic:
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b
    
    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

if __name__ == '__main__':
    calc = BasicArithmetic()
    num1 = 10
    num2 = 5
    sum_result = calc.add(num1, num2)
    diff_result = calc.subtract(num1, num2)
    print(f"Addition: {sum_result}")
    print(f"Subtraction: {diff_result}")