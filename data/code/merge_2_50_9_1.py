from typing import Any
class Adder:
    def add(self, a: int, b: int, c: int) -> int:
        return a + b + c
def create_adder() -> Adder:
    return Adder()
if __name__ == '__main__':
    service = create_adder()
    result = service.add(10, 20, 30)
    print(result)