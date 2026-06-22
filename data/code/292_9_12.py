class Kite:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @staticmethod
    def calculate_perimeter(side_a, side_b):
        return 2 * (side_a + side_b)

if __name__ == '__main__':
    kite = Kite(5, 7)
    perimeter = kite.calculate_perimeter(kite.side_a, kite.side_b)
    print(perimeter)