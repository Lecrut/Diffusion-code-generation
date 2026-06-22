class Prism:
    def __init__(self, base_area, height):
        if not isinstance(base_area, (int, float)) or base_area <= 0:
            raise ValueError("Base area must be a positive number")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number")
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    test_prism = Prism(42, 15)
    print(test_prism.get_volume())