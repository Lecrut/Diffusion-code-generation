from typing import List
class Calculator:
    def add(self, numbers: List[float]) -> float:
        return sum(numbers)
def create_calculator() -> Calculator:
    return Calculator()
if __name__ == '__main__':
    calculator = create_calculator()
    result = calculator.add([10.5, 20.3, 30.7])
    print(result)