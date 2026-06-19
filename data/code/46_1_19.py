class Triangle:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle = Triangle(6, 8, 10)
    print(triangle.perimeter())