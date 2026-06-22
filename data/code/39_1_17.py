class Prism:
    def __init__(self, base_area: float, height: float) -> None:
        self.base_area = base_area
        self.height = height

    def calculate_volume(self) -> float:
        if self.base_area < 0 or self.height < 0:
            raise ValueError("Base area and height must be non-negative.")
        return self.base_area * self.height

if __name__ == '__main__':
    sample_base_area = 15.5
    sample_height = 8.0
    prism_instance = Prism(sample_base_area, sample_height)
    print(prism_instance.calculate_volume())