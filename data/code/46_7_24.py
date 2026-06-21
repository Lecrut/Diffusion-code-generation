class Triangle:
    MIN_SIDE_LENGTH = 1

    @staticmethod
    def validate_sides(sides):
        if any(side <= Triangle.MIN_SIDE_LENGTH for side in sides):
            raise ValueError("All sides must be positive numbers.")

    @staticmethod
    def calculate_perimeter(sides):
        Triangle.validate_sides(sides)
        return sum(sides)

if __name__ == '__main__':
    sample_triangle_sides = [5, 12, 13]
    perimeter = Triangle.calculate_perimeter(sample_triangle_sides)
    print(perimeter)