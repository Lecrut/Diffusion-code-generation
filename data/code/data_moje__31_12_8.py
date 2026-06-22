class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def display_result(self):
        print(self.get_area())

if __name__ == '__main__':
    SIDE_LENGTH = 7
    shape = Square(SIDE_LENGTH)
    shape.display_result()