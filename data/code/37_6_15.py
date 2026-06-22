class Parallelogram:
    area_multiplier = 1

    def compute_area(self, base, height):
        if not isinstance(base, (int, float)) or isinstance(base, bool):
            raise TypeError("Base must be numeric")
        if not isinstance(height, (int, float)) or isinstance(height, bool):
            raise TypeError("Height must be numeric")
        if base <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        calculated_area = base * height * self.area_multiplier
        return calculated_area

if __name__ == '__main__':
    shape = Parallelogram()
    base_length = 12.5
    height_length = 8.0
    area_result = shape.compute_area(base_length, height_length)
    print(area_result)