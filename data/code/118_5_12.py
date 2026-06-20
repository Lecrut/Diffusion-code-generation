from typing import Union

class MathOperations:
    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply(6, 7.5)
    print(result)