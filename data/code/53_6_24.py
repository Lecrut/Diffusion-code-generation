class Square:
    def __init__(self, area):
        self.area = area

    @staticmethod
    def find_side_length(area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        return area ** 0.5

    def get_side_length(self):
        return Square.find_side_length(self.area)

if __name__ == '__main__':
    sample_area = 64
    square = Square(sample_area)
    side_length = square.get_side_length()
    print(side_length)