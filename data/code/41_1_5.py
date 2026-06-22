from dataclasses import dataclass

@dataclass(frozen=True)
class Rhombus:
    diagonal1: float
    diagonal2: float

    def area(self) -> float:
        return self.diagonal1 * self.diagonal2 / 2.0

def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    rhombus = Rhombus(diagonal1, diagonal2)
    return rhombus.area()

if __name__ == '__main__':
    diag1: float = 10.0
    diag2: float = 8.0
    result: float = calculate_rhombus_area(diag1, diag2)
    print(result)