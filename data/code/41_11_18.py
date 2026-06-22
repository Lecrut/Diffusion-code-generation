class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Diagonals must be positive numbers.")
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def compute_area(self):
        return (self.diagonal1 * self.diagonal2) / 2

if __name__ == '__main__':
    r = Rhombus(10, 8)
    print(r.compute_area())
    r2 = Rhombus(5.5, 3.2)
    print(r2.compute_area())