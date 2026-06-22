class Kite:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    @staticmethod
    def perimeter(side1, side2):
        return 2 * (side1 + side2)

if __name__ == '__main__':
    kite = Kite(5, 7)
    perimeter = Kite.perimeter(kite.side1, kite.side2)
    print(perimeter)