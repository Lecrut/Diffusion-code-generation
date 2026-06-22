from typing import Union

Number = Union[int, float]

class Parallelogram:
    def __init__(self, base: Number, height: Number) -> None:
        if base < 0:
            raise ValueError("Base cannot be negative")
        if height < 0:
            raise ValueError("Height cannot be negative")
        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height

if __name__ == "__main__":
    base_value = 10.5
    height_value = 7.2
    shape = Parallelogram(base_value, height_value)
    print(shape.area())