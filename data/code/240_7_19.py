class Square:
    SIDE_LENGTH = 12

    @staticmethod
    def area():
        return Square.SIDE_LENGTH ** 2

if __name__ == '__main__':
    print(f"The area of a square with side {Square.SIDE_LENGTH} is: {Square.area()}")