from typing import Union

class Calculator:
    @staticmethod
    def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

if __name__ == '__main__':
    print(Calculator.add_numbers(3, 4))
    print(Calculator.add_numbers(5.5, 2.1))