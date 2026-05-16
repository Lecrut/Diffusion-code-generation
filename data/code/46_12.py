class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculate_perimeter(self):
        return self.a + self.b + self.c
if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    perimeter = t.calculate_perimeter()
    print(perimeter)