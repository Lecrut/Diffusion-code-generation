class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def side_length(self):
        return self.area ** 0.5

    def perimeter(self):
        return 4 * self.side_length()

if __name__ == '__main__':
    sample_area = 25.0
    square = Square(sample_area)
    print("Side Length:", square.side_length())
    print("Perimeter:", square.perimeter())