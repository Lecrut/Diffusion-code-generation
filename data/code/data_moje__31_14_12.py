class SquareGeometry:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    geometry = SquareGeometry(50)
    area_value = geometry.get_area()
    print(area_value)