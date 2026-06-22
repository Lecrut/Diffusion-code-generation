class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    
    @staticmethod
    def area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_side = 10
    square_area = Square.area(sample_side)
    print(square_area)