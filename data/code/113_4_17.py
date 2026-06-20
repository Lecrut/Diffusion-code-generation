from typing import Union

class ArithmeticOperations:
    MIN_VALUE = -1000

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if a < ArithmeticOperations.MIN_VALUE or b < ArithmeticOperations.MIN_VALUE:
            raise ValueError('Values must be greater than or equal to -1000')
        return a - b
if __name__ == '__main__':
    result = ArithmeticOperations.subtract(15, 7)
    print(result)