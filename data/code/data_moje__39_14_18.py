class PrismCalculator:
    def __init__(self):
        self.volume_cache = {}

    def calculate_volume(self, base_area, height):
        if base_area < 0 or height < 0:
            raise ValueError("Base area and height must be non-negative.")
        volume = base_area * height
        self.volume_cache[(base_area, height)] = volume
        return volume

if __name__ == '__main__':
    calculator = PrismCalculator()
    test_cases = [
        {"base_area": 36, "height": 12},
        {"base_area": 10, "height": 4},
        {"base_area": 0, "height": 100}
    ]
    for case in test_cases:
        vol = calculator.calculate_volume(case["base_area"], case["height"])
        print(vol)