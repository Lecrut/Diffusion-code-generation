class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self.is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def is_valid_triangle(self):
        return (self.sides[0] + self.sides[1] > self.sides[2] and
                self.sides[0] + self.sides[2] > self.sides[1] and
                self.sides[1] + self.sides[2] > self.sides[0])

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print(triangle1.perimeter())
    triangle2 = Triangle(6, 8, 10)
    print(triangle2.perimeter())
    triangle3 = Triangle(7, 10, 5)
    try:
        print(triangle3.perimeter())
    except ValueError as e:
        print(e)