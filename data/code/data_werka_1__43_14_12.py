class Square:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def calculate_area(side):
        if side <= Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be greater than zero.")
        return side * side

if __name__ == '__main__':
    sides = [5, 10.5, -3, 0]
    for side in sides:
        try:
            area = Square.calculate_area(side)
            print(f"The area of a square with side {side} is: {area}")
        except ValueError as e:
            print(f"Error for side {side}: {e}")