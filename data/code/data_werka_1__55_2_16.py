class Triangle:
    def __init__(self, a, b, c):
        self.sides = {'a': a, 'b': b, 'c': c}
        self._validate_sides()

    def _validate_sides(self):
        if not (self.sides['a'] + self.sides['b'] > self.sides['c'] and
                self.sides['a'] + self.sides['c'] > self.sides['b'] and
                self.sides['b'] + self.sides['c'] > self.sides['a']):
            raise ValueError("The given side lengths do not form a valid triangle.")

    def get_perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    try:
        t1 = Triangle(3, 4, 5)
        print(f"Perimeter of triangle (3, 4, 5): {t1.get_perimeter()}")
    except ValueError as e:
        print(e)

    try:
        t2 = Triangle(1, 2, 10)
        print(f"Perimeter of triangle (1, 2, 10): {t2.get_perimeter()}")
    except ValueError as e:
        print(e)