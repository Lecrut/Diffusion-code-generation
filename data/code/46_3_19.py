import argparse

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.validate()

    def validate(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("Side lengths must be positive.")
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise ValueError("The given side lengths do not form a valid triangle.")

    def perimeter(self):
        return self.a + self.b + self.c

def main():
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f"Perimeter of (3, 4, 5): {triangle1.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle2 = Triangle(1, 2, 3)
        print(f"Perimeter of (1, 2, 3): {triangle2.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()