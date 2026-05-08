from typing import Union
class QuantityCalculator:
    def add(self, quantity1: Union[int, float], quantity2: Union[int, float]) -> Union[int, float]:
        return quantity1 + quantity2
if __name__ == '__main__':
    calculator = QuantityCalculator()
    a = 10
    b = 5.5
    result = calculator.add(a, b)
    print(result)