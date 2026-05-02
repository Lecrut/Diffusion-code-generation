import math
class ScalableVolume:
    def __init__(self, base_volume, scale_factor=1.0):
        self.base_volume = float(base_volume)
        self.scale_factor = float(scale_factor)
    def get_volume(self):
        return self.base_volume * self.scale_factor
    def scale(self, factor):
        self.scale_factor *= factor
    def set_scale_factor(self, factor):
        self.scale_factor = float(factor)
if __name__ == '__main__':
    data = [
        (10.0, 2.0),
        (5.5, 1.5),
        (100.0, 1.0),
        (0.1, 3.0)
    ]
    volume_storage = []
    for base_v, scale_f in data:
        sv = ScalableVolume(base_v, scale_f)
        volume_storage.append(sv)
    print("--- Initial Volumes ---")
    for sv in volume_storage:
        print(f"Base: {sv.base_volume}, Scale: {sv.scale_factor}, Actual: {sv.get_volume()}")
    print("\n--- Scaling Example ---")
    item_to_scale = volume_storage[0]
    print(f"Original Item 1: Base={item_to_scale.base_volume}, Scale={item_to_scale.scale_factor}, Volume={item_to_scale.get_volume()}")
    new_scale = 2.5
    item_to_scale.scale(new_scale)
    print(f"Scaled Item 1 (Scale by {new_scale}): Base={item_to_scale.base_volume}, Scale={item_to_scale.scale_factor}, Volume={item_to_scale.get_volume()}")
    item_to_scale = volume_storage[2]
    print(f"Original Item 3: Base={item_to_scale.base_volume}, Scale={item_to_scale.scale_factor}, Volume={item_to_scale.get_volume()}")
    new_scale_2 = 0.5
    item_to_scale.scale(new_scale_2)
    print(f"Scaled Item 3 (Scale by {new_scale_2}): Base={item_to_scale.base_volume}, Scale={item_to_scale.scale_factor}, Volume={item_to_scale.get_volume()}")
    print("\n--- Final State of Storage ---")
    for sv in volume_storage:
        print(f"Base: {sv.base_volume}, Scale: {sv.scale_factor}, Volume: {sv.get_volume()}")