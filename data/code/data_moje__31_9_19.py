class Square:
    SIDE_UNIT = "units"
    
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self._side_length = side_length
    
    @staticmethod
    def _compute_area(base):
        return base * base
    
    def area(self):
        return self._compute_area(self._side_length)

if __name__ == '__main__':
    test_length = 7
    my_square = Square(test_length)
    result = my_square.area()
    print(result)