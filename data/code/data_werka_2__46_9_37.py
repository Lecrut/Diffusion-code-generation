class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side_lengths = {'side1': side1, 'side2': side2, 'side3': side3}

    def perimeter(self) -> float:
        return sum(self.side_lengths.values())

if __name__ == '__main__':
    triangle = Triangle(7.0, 9.0, 12.0)
    print(triangle.perimeter())