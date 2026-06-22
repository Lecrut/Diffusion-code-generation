class Square:
    side_length = 10

    @staticmethod
    def calculate_area():
        return Square.side_length * Square.side_length

if __name__ == '__main__':
    area = Square.calculate_area()
    print(area)