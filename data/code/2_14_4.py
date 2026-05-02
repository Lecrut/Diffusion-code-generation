import math
class ScalableVolume:
    def __init__(self, base_volume, scaling_factor):
        self.base_volume = base_volume
        self.scaling_factor = scaling_factor
    def get_volume(self, factor):
        return self.base_volume * factor
    def get_scaled_volume(self, factor):
        return self.base_volume * self.scaling_factor * factor
if __name__ == '__main__':
    data = [
        ScalableVolume(10.0, 2.0),
        ScalableVolume(5.5, 1.5),
        ScalableVolume(100.0, 1.0),
        ScalableVolume(3.14159, 3.0)
    ]
    print("--- Stored Scalable Volume Data ---")
    for item in data:
        print(f"Base: {item.base_volume}, Scale: {item.scaling_factor}")
    print("\n--- Retrieving Volumes ---")
    test_factor = 5.0
    for i, volume_obj in enumerate(data):
        actual = volume_obj.get_volume(test_factor)
        scaled = volume_obj.get_scaled_volume(test_factor)
        print(f"Item {i}: Base Volume = {volume_obj.base_volume}, Scaled Volume (Factor {test_factor}) = {actual}, Scaled Volume (Factor {test_factor} applied) = {scaled}")
    test_factor_2 = 10.0
    print(f"\n--- Retrieving Volumes with Factor {test_factor_2} ---")
    for i, volume_obj in enumerate(data):
        actual = volume_obj.get_volume(test_factor_2)
        scaled = volume_obj.get_scaled_volume(test_factor_2)
        print(f"Item {i}: Base Volume = {volume_obj.base_volume}, Scaled Volume (Factor {test_factor_2}) = {actual}, Scaled Volume (Factor {test_factor_2} applied) = {scaled}")