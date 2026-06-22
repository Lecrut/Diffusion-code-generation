class Triangle:
    def __init__(self, **sides):
        if len(sides) != 3:
            raise ValueError("Exactly three sides are required")
        self.sides = {k: v for k, v in sides.items()}
        self.validate_sides()

    def validate_sides(self):
        a, b, c = self.sides.values()
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    try:
        triangle = Triangle(side1=3, side2=4, side3=5)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)