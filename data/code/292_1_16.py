class Square:
    SIDES_COUNT = 4

    @staticmethod
    def calculate_perimeter(side_length):
        return side_length * Square.SIDES_COUNT

if __name__ == '__main__':
    sample_side1 = 3
    result1 = Square.calculate_perimeter(sample_side1)
    print(f"Perimeter of a square with side {sample_side1}: {result1}")

    sample_side2 = 5
    result2 = Square.calculate_perimeter(sample_side2)
    print(f"Perimeter of a square with side {sample_side2}: {result2}")