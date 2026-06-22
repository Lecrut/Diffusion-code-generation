class Rhombus:
    def __init__(self, d1, d2):
        if d1 <= 0 or d2 <= 0:
            raise ValueError("Diagonals must be positive numbers")
        self.d1 = d1
        self.d2 = d2

    def compute_area(self):
        return 0.5 * self.d1 * self.d2

if __name__ == '__main__':
    rhombus = Rhombus(10, 8)
    print(rhombus.compute_area())