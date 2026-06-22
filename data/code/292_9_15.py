class Kite:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def calculate_perimeter(self):
        return 2 * (self.side1 + self.side2)

if __name__ == '__main__':
    kite_instance = Kite(5, 7)
    perimeter = kite_instance.calculate_perimeter()
    print(perimeter)