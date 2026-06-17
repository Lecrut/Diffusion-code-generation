from typing import Any
class Adder:
    def add(self, a: float, b: float, c: float) -> float:
        return a + b + c
def create_adder() -> Adder:
    return Adder()
if __name__ == '__main__':
    adder = create_adder()
    result = adder.add(10.5, 20.3, 30.7)
    print(result)