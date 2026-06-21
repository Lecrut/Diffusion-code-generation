SIDE_LENGTH = 7.5

class SquareAreaCalculator:
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side length must be positive")
        self._side = side

    def get_area(self) -> float:
        return self._side ** 2

if __name__ == '__main__':
    calculator = SquareAreaCalculator(SIDE_LENGTH)
    print(calculator.get_area())