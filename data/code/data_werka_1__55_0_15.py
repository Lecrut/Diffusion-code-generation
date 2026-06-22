class Triangle:
    def __init__(self, a, b, c):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("Side lengths must be positive.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The side lengths do not form a valid triangle.")
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(f"Error: {e}")