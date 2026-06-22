class TriangleCalculator:
    AREA_FACTOR = 0.5

    @staticmethod
    def compute_area(base: float, height: float) -> float:
        if base <= 0.0 or height <= 0.0:
            raise ValueError("Base and height must be positive.")
        return TriangleCalculator.AREA_FACTOR * base * height

if __name__ == '__main__':
    CALCULATOR = TriangleCalculator()
    TEST_BASE = 12.5
    TEST_HEIGHT = 8.0
    RESULT = CALCULATOR.compute_area(TEST_BASE, TEST_HEIGHT)
    print(RESULT)