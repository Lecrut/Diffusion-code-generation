class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side_lengths = [side1, side2, side3]

    @staticmethod
    def validate_side_length(side: float) -> bool:
        return side > 0

    def perimeter(self) -> float:
        if all(Triangle.validate_side_length(side) for side in self.side_lengths):
            return sum(self.side_lengths)
        else:
            raise ValueError("All sides must be greater than zero.")

if __name__ == '__main__':
    triangle = Triangle(7.0, 9.0, 12.0)
    print(triangle.perimeter())