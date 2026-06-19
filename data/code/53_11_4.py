import math

class Square:
    def __init__(self):
        self._area = 16.0

    @property
    def side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    square = Square()
    print(square.side_length)