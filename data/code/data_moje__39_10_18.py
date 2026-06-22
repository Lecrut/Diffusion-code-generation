class Prism:
    def __init__(self, base_area, height):
        if base_area < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.base_area = base_area
        self.height = height

    def validate_state(self):
        return self.base_area >= 0 and self.height >= 0

    def volume(self):
        if not self.validate_state():
            raise RuntimeError("Invalid prism dimensions")
        return self.base_area * self.height

if __name__ == '__main__':
    prism = Prism(12.5, 4.0)
    print(prism.volume())