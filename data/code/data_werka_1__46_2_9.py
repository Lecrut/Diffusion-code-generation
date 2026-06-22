class Triangle:
    MIN_SIDE_LENGTH = 0.01

    @staticmethod
    def validate_side_lengths(a, b, c):
        if not all(isinstance(x, (int, float)) and x > Triangle.MIN_SIDE_LENGTH for x in [a, b, c]):
            raise ValueError("Side lengths must be positive numbers greater than zero.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given side lengths do not form a valid triangle.")

    def __init__(self, a, b, c):
        Triangle.validate_side_lengths(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        t = Triangle(3, 4, 5)
        perimeter = t.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)