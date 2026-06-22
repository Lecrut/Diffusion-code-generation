class Triangle:
    @staticmethod
    def is_valid(side1, side2, side3):
        return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

    @staticmethod
    def calculate_perimeter(side1, side2, side3):
        if not Triangle.is_valid(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        return side1 + side2 + side3

if __name__ == '__main__':
    try:
        result1 = Triangle.calculate_perimeter(3, 4, 5)
        print(f"Perimeter for sides 3, 4, 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = Triangle.calculate_perimeter(7, 10, 5)
        print(f"Perimeter for sides 7, 10, 5: {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = Triangle.calculate_perimeter(-1, 4, 5)
        print(f"Perimeter for sides -1, 4, 5: {result3}")
    except ValueError as e:
        print(f"Error: {e}")