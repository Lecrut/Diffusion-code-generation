from typing import Union

Number = Union[int, float]

class Parallelogram:
    def __init__(self, base: Number, height: Number) -> None:
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.base = base
        self.height = height

    def get_area(self) -> Number:
        return self.base * self.height

def compute_parallelogram_area(base: Number, height: Number) -> Number:
    return base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    print(compute_parallelogram_area(sample_base, sample_height))
    instance = Parallelogram(sample_base, sample_height)
    print(instance.get_area())