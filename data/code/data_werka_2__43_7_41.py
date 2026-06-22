class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError("Side length must be a non-negative number")
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        square1 = Square(4)
        print(f"Area of square with side 4: {square1.get_area()}")

        square2 = Square(6.5)
        print(f"Area of square with side 6.5: {square2.get_area()}")
    except ValueError as e:
        print(e)