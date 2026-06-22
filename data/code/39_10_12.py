class Prism:
    def __init__(self, base_area, height):
        self._validate_base_area(base_area)
        self._validate_height(height)
        self.base_area = base_area
        self.height = height

    def _validate_base_area(self, area):
        if not isinstance(area, (int, float)):
            raise TypeError("Base area must be a number")
        if area < 0:
            raise ValueError("Base area must be non-negative")

    def _validate_height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number")
        if height < 0:
            raise ValueError("Height must be non-negative")

    def calculate_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    sample_base = 24.5
    sample_height = 8.0
    my_prism = Prism(sample_base, sample_height)
    result = my_prism.calculate_volume()
    print(result)