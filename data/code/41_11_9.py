class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        if not isinstance(diagonal1, (int, float)) or not isinstance(diagonal2, (int, float)):
            raise TypeError("Diagonals must be numbers")
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Diagonals must be positive numbers")
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def get_area(self):
        return 0.5 * self.diagonal1 * self.diagonal2

if __name__ == '__main__':
    rhombus = Rhombus(10, 12)
    area = rhombus.get_area()
    print(area)