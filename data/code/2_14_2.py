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
        ScalableVolume(3.14159, 3.0)
    ]
    print("--- Stored Scalable Volume Data ---")
    for i, vol_obj in enumerate(data):
        print(f"Item {i}: Base={vol_obj.base_volume}, Scale={vol_obj.scale_factor}")
    print("\n--- Retrieval Examples ---")
    item1 = data[0]
    print(f"Item 0 Base Volume: {item1.base_volume}")
    factor_to_retrieve = 5.0
    retrieved_volume = item1.get_volume(factor_to_retrieve)
    print(f"Item 0 Volume scaled by {factor_to_retrieve}: {retrieved_volume}")
    multiplier = 2.5
    scaled_volume = item1.get_scaled_volume(multiplier)
    print(f"Item 0 Scaled Volume (Base * Scale * Multiplier): {scaled_volume}")
    item3 = data[2]
    print(f"Item 2 Base Volume: {item3.base_volume}")
    retrieved_volume_3 = item3.get_volume(10)
    print(f"Item 2 Volume scaled by 10: {retrieved_volume_3}")