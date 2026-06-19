import math

class Square:
    AREA = 16.0
    
    @staticmethod
    def compute_side_length(area):
        return math.sqrt(area)
    
    @property
    def side_length(self):
        return self.compute_side_length(self.AREA)

if __name__ == '__main__':
    default_square = Square()
    print(default_square.side_length)