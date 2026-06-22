class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length

if __name__ == '__main__':
    side1 = 7.0
    square_instance = Square(side1)
    area_result = square_instance.get_area()
    print(f"Area of the square with side {side1} is: {area_result}")

    side2 = 3.5
    another_square = Square(side2)
    area_of_another_square = another_square.get_area()
    print(f"Area of the square with side {side2} is: {area_of_another_square}")