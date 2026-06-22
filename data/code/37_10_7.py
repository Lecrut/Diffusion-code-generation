from typing import Union

Number = Union[int, float]

class Parallelogram:
    def __init__(self, base: Number, height: Number) -> None:
        self._base: Number = base
        self._height: Number = height

    @property
    def base(self) -> Number:
        return self._base

    @property
    def height(self) -> Number:
        return self._height

    def area(self) -> float:
        return float(self._base * self._height)

def compute_area(base: Number, height: Number) -> float:
    return float(base * height)

if __name__ == '__main__':
    base_value: Number = 10.0
    height_value: Number = 5.0

    result_func: float = compute_area(base_value, height_value)
    print(result_func)

    shape: Parallelogram = Parallelogram(base=12.5, height=4.0)
    result_class: float = shape.area()
    print(result_class)