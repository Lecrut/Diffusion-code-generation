class Rhombus:
    def __init__(self, d1, d2):
        if not isinstance(d1, (int, float)) or not isinstance(d2, (int, float)):
            raise TypeError("Diagonals must be numbers")
        if d1 <= 0 or d2 <= 0:
            raise ValueError("Diagonals must be positive numbers")
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return (self.d1 * self.d2) / 2

if __name__ == '__main__':
    rhombus = Rhombus(10, 8)
    print(rhombus.area())