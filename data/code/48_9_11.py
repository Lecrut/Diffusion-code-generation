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
                return a * 4
            else:
                p = sum(self.sides)
                s1 = (p / 2 + a - b) * (p / 2 + a - c) * (p / 2 + a - d) * (p / 2 - a + b + c + d)
                return (s1 ** 0.5) / 4
        elif len(self.sides) == 5:
            return sum(self.sides)
        elif len(self.sides) == 6:
            s = sum(self.sides) / 2
            return (s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]) * 
                    (s - self.sides[3]) * (s - self.sides[4])) ** 0.5 / 4
        else:
            return "Area calculation not supported for this shape"

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")

    square = Shape([4] * 4)
    print(f"Square Perimeter: {square.perimeter()}")
    print(f"Square Area: {square.area()}")

    pentagon = Shape([2] * 5)
    print(f"Pentagon Perimeter: {pentagon.perimeter()}")
    print(f"Pentagon Area: {pentagon.area()}")

    hexagon = Shape([3, 3, 3, 3, 3, 3])
    print(f"Hexagon Perimeter: {hexagon.perimeter()}")
    print(f"Hexagon Area: {hexagon.area()}")