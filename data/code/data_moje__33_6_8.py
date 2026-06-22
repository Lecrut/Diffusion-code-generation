from typing import Union

Number = Union[int, float]
HALF_CONSTANT: float = 0.5

def validate_positive(value: Number) -> None:
    if value <= 0:
        raise ValueError("Dimensions must be positive")

def calculate_triangle_area(base: Number, height: Number) -> float:
    validate_positive(base)
    validate_positive(height)
    return base * height * HALF_CONSTANT

class Triangle:
    def __init__(self, base: Number, height: Number) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        validate_positive(self.base)
        validate_positive(self.height)
        return self.base * self.height * HALF_CONSTANT

if __name__ == '__main__':
    sample_base = 12
    sample_height = 7.5
    triangle_instance = Triangle(sample_base, sample_height)
    print(triangle_instance.area())