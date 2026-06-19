class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    side_length1 = 5
    area1 = Square.calculate_area(side_length1)
    print((side_length1, area1))

    side_length2 = 10.5
    area2 = Square.calculate_area(side_length2)
    print((side_length2, area2))