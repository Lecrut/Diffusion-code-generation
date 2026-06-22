class Parallelogram:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)):
            raise TypeError("Base must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number")
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self._base = base
        self._height = height

    def calculate_area(self):
        return self._base * self._height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    shape = Parallelogram(base_value, height_value)
    result = shape.calculate_area()
    print(result)