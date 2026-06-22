class Triangle:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def validate_sides(sides):
        if any(side <= Triangle.MIN_SIDE_LENGTH for side in sides):
            raise ValueError("All sides must be positive numbers.")

    def __init__(self, sides):
        Triangle.validate_sides(sides)
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_triangle = Triangle([3, 4, 5])
    perimeter = sample_triangle.calculate_perimeter()
    print(perimeter)