class InvalidLengthException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.reason = msg

class MeasurementUnit:
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y

    def validate_dimensions(self):
        if self.dim_x < 0:
            raise InvalidLengthException("X dimension cannot be negative")
        if self.dim_y < 0:
            raise InvalidLengthException("Y dimension cannot be negative")
        if abs(self.dim_x - self.dim_y) > 1000000:
            raise InvalidLengthException("Dimensions are impossibly far apart")
        return True

    def get_average(self):
        self.validate_dimensions()
        return (self.dim_x + self.dim_y) / 2.0

if __name__ == '__main__':
    unit = MeasurementUnit(10.5, 20.5)
    avg = unit.get_average()
    print(avg)