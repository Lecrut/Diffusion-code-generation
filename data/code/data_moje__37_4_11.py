class ParallelogramCalculator:
    _formula_factor = 1.0

    @staticmethod
    def get_parallelogram_area(base: float, height: float) -> float:
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        return base * height * ParallelogramCalculator._formula_factor

if __name__ == '__main__':
    sample_base = 8.5
    sample_height = 4.2
    result = ParallelogramCalculator.get_parallelogram_area(sample_base, sample_height)
    print(result)