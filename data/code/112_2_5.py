from typing import Union
class QuantityCalculator:
    def add(self, quantity1: Union[int, float], quantity2: Union[int, float]) -> Union[int, float]:
        return quantity1 + quantity2
if __name__ == '__main__':
    calculator = QuantityCalculator()
    result1 = calculator.add(10, 5)
    print(f"10 + 5 = {result1}")
    result2 = calculator.add(3.5, 1.2)
    print(f"3.5 + 1.2 = {result2}")
    result3 = calculator.add(-10, 20)
    print(f"-10 + 20 = {result3}")