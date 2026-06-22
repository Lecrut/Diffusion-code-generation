class Prism:
    MINIMUM_VALID_VALUE = 0
    
    def __init__(self, base_area, height):
        if not isinstance(base_area, (int, float)) or base_area <= self.MINIMUM_VALID_VALUE:
            raise ValueError("Base area must be a positive number")
        if not isinstance(height, (int, float)) or height <= self.MINIMUM_VALID_VALUE:
            raise ValueError("Height must be a positive number")
        self.base_area = float(base_area)
        self.height = float(height)
    
    def calculate_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    sample_base = 12.5
    sample_height = 8.0
    my_prism = Prism(sample_base, sample_height)
    computed_volume = my_prism.calculate_volume()
    print(computed_volume)