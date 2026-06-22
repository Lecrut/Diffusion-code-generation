def compute_prism_volume(base_area: float, height: float) -> float:
    if base_area <= 0:
        raise ValueError("Base area must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return base_area * height

class Prism:
    def __init__(self, base_area: float, height: float):
        self.base_area = base_area
        self.height = height
    
    def get_volume(self) -> float:
        return compute_prism_volume(self.base_area, self.height)

if __name__ == '__main__':
    sample_base_area = 25.5
    sample_height = 10.0
    calculated_volume = compute_prism_volume(sample_base_area, sample_height)
    print(calculated_volume)
    prism_instance = Prism(sample_base_area, sample_height)
    print(prism_instance.get_volume())