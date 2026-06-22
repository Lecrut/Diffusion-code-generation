class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    sample_values = [3, 4, 5]
    for length in sample_values:
        print(f"Area of square with side {length}: {Square.area(length)}")