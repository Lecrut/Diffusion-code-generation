class Rhombus:
    def __init__(self, d1, d2):
        if d1 <= 0 or not isinstance(d1, (int, float)):
            raise ValueError("Diagonal d1 must be a positive number")
        if d2 <= 0 or not isinstance(d2, (int, float)):
            raise ValueError("Diagonal d2 must be a positive number")
        self.d1 = d1
        self.d2 = d2

    def compute_area(self):
        return 0.5 * self.d1 * self.d2

if __name__ == '__main__':
    rhombus = Rhombus(10, 8)
    print(rhombus.compute_area())