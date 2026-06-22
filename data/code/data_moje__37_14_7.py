GEOMETRY_CONSTANTS = {
    'parallelogram_area_formula': 'base_times_height'
}

class ParallelogramMetrics:
    def __init__(self, base: float, height: float) -> None:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return self.base * self.height

if __name__ == '__main__':
    constant_base = 12.0
    constant_height = 6.0
    shape = ParallelogramMetrics(constant_base, constant_height)
    computed_area = shape.calculate_area()
    print(computed_area)