def calculate_prism_volume(base_area, height):
    if base_area < 0:
        raise ValueError("Base area cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return base_area * height

class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return calculate_prism_volume(self.base_area, self.height)

if __name__ == '__main__':
    SAMPLE_BASE = 12.5
    SAMPLE_HEIGHT = 4.2
    p = Prism(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(p.get_volume())