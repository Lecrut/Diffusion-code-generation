class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        side_value = 8
        square_instance = Square(side_value)
        area_result = square_instance.compute_area()
        print(f"The area of the square with side length {side_value} is: {area_result}")
    except ValueError as e:
        print(e)