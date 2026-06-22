class Square:
    @staticmethod
    def area(side):
        return side * side

if __name__ == '__main__':
    sample_side = 7
    result = Square.area(sample_side)
    print(result)