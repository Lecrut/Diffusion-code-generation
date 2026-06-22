import math

class Square:
    _AREA = 16.0
    
    def __init__(self):
        self._side_length = math.sqrt(self._AREA)
    
    @property
    def side_length(self):
        return self._side_length

if __name__ == '__main__':
    square = Square()
    print(square.side_length)