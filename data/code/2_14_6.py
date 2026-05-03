import math
class ScalableVolume:
    def __init__(self, base_volume, scale_factor):
        self.base_volume = base_volume
        self.scale_factor = scale_factor
    def get_volume(self, factor):
        return self.base_volume * factor
    def get_scaled_volume(self, multiplier):
        return self.base_volume * (self.scale_factor * multiplier)
if __name__ == '__main__':
    data = [
        ScalableVolume(10.0, 2.0),
        ScalableVolume(5.5, 1.5),
        ScalableVolume(100.0, 1.0),
        ScalableVolume(3.14159, 2.5)
    ]
    print("--- Stored Data ---")
    for item in data:
        print(f"Base: {item.base_volume}, Scale: {item.scale_factor}")
    print("\n--- Retrieval Examples ---")
    item1 = data[0]
    print(f"Item 1 Base Volume: {item1.base_volume}")
    factor_of_3 = 3.0
    volume_3 = item1.get_volume(factor_of_3)
    print(f"Item 1 Volume scaled by {factor_of_3}: {volume_3}")
    multiplier = 2.0
    scaled_volume = item1.get_scaled_volume(multiplier)
    print(f"Item 1 Scaled Volume (using multiplier {multiplier}): {scaled_volume}")
    item3 = data[2]
    print(f"Item 3 Scaled Volume (using multiplier 4.0): {item3.get_scaled_volume(4.0)}")