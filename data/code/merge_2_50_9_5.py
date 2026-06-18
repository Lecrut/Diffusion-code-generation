from typing import Union
class Calculator:
    def add(self, a: float, b: float, c: float) -> float:
        return a + b + c
def create_calculator() -> Calculator:
    calculator = Calculator()
    return calculator
if __name__ == '__main__':
    calc_instance = create_calculator()
    result = calc_instance.add(10.5, 20.3, 30.7)
    print(result)