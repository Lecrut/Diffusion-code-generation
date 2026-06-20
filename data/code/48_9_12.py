class Shape:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        if len(self.sides) == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        elif len(self.sides) == 4:
            a, b, c, d = self.sides
            if a == b == c == d:
                return a * b
            else:
                p = sum(self.sides)
                s1, s2 = (p / 2), (p - a + b + c) / 2
                s3, s4 = (s2 + a - b) / 2, (s2 - a + b) / 2
                return (s1 * s3) ** 0.5 + (s1 * s4) ** 0.5

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print("Perimeter:", triangle.perimeter())
    print("Area:", triangle.area())

    square = Shape([5, 5, 5, 5])
    print("Perimeter:", square.perimeter())
    print("Area:", square.area())