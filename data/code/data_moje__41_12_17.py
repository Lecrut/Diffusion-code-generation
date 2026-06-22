DIAGONAL_MULTIPLIER = 0.5

class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def get_area(self):
        return DIAGONAL_MULTIPLIER * self.diagonal1 * self.diagonal2

if __name__ == '__main__':
    shape = Rhombus(6.0, 8.0)
    print(shape.get_area())