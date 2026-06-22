class Rhombus:
    def __init__(self, d1, d2):
        if d1 <= 0:
            raise ValueError("Diagonal 1 must be a positive number")
        if d2 <= 0:
            raise ValueError("Diagonal 2 must be a positive number")
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return 0.5 * self.d1 * self.d2

if __name__ == '__main__':
    r = Rhombus(10, 6)
    print(r.area())