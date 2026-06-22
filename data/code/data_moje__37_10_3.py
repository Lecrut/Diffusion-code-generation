from typing import Union

Number = Union[int, float]

class Parallelogram:
    def __init__(self, base: Number, height: Number) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> Number:
        return self.base * self.height

if __name__ == '__main__':
    sample_base = 10.5
    sample_height = 4.2
    shape = Parallelogram(sample_base, sample_height)
    print(shape.calculate_area())