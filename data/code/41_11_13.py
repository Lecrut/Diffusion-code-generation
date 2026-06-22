class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        if diagonal1 <= 0:
            raise ValueError("Diagonal1 must be a positive number")
        if diagonal2 <= 0:
            raise ValueError("Diagonal2 must be a positive number")
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def get_area(self):
        return 0.5 * self.diagonal1 * self.diagonal2

if __name__ == '__main__':
    rhombus = Rhombus(10, 8)
    print(rhombus.get_area())