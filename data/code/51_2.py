class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths
    def calculate_perimeter(self):
        return sum(self.side_lengths)
if __name__ == '__main__':
    sides1 = [3, 4, 5]
    poly1 = Polygon(sides1)
    perimeter1 = poly1.calculate_perimeter()
    print(f"Perimeter of Polygon 1: {perimeter1}")
    sides2 = [10, 20, 30, 40]
    poly2 = Polygon(sides2)
    perimeter2 = poly2.calculate_perimeter()
    print(f"Perimeter of Polygon 2: {perimeter2}")