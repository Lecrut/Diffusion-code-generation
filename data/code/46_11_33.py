class Triangle:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def validate_side_length(side):
        if side <= Triangle.MIN_SIDE_LENGTH:
            raise ValueError("Side lengths must be positive numbers.")

    @staticmethod
    def calculate_perimeter(side1, side2, side3):
        Triangle.validate_side_length(side1)
        Triangle.validate_side_length(side2)
        Triangle.validate_side_length(side3)
        return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        perimeter = Triangle.calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)