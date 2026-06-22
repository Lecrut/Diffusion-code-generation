from dataclasses import dataclass

SQUARE_OPERATOR = 2

@dataclass
class GeometryCalculator:
    side_length: float

    def calculate_square(self) -> float:
        return self.side_length ** SQUARE_OPERATOR

if __name__ == '__main__':
    FIXED_INPUT = 10
    calculator = GeometryCalculator(FIXED_INPUT)
    print(calculator.calculate_square())