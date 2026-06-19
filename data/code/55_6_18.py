class Triangle:
    @staticmethod
    def calculate_perimeter(a, b, c):
        return a + b + c

if __name__ == '__main__':
    sides = [7, 10, 5]
    perimeter = Triangle.calculate_perimeter(*sides)
    print(perimeter)