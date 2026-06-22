from dataclasses import dataclass
from typing import Union

Number = Union[int, float]

@dataclass
class Triangle:
    base: Number
    height: Number

    def area(self) -> float:
        return 0.5 * float(self.base) * float(self.height)

    def perimeter_estimate(self, side_a: Number, side_b: Number) -> float:
        return float(self.base) + float(side_a) + float(side_b)

if __name__ == '__main__':
    t = Triangle(base=12, height=8)
    print(t.area())
    print(t.perimeter_estimate(10, 15))