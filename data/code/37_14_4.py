class Parallelogram:
    def __init__(self, base: float, height: float) -> None:
        if base < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self._base = base
        self._height = height

    def area(self) -> float:
        return self._base * self._height

if __name__ == '__main__':
    SHAPE = Parallelogram(15.0, 4.0)
    print(SHAPE.area())