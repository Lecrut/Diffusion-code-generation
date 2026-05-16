import math
class ScalableVolumeData:
    def __init__(self, base_volume, scaling_factor):
        self.base_volume = base_volume
        self.scaling_factor = scaling_factor
        self.scaled_volume = base_volume
    def get_volume(self):
        return self.scaled_volume
    def scale(self, factor):
        self.scaling_factor = factor
        self.scaled_volume = self.base_volume * factor
    def get_base_volume(self):
        return self.base_volume
    def get_scaling_factor(self):
        return self.scaling_factor
if __name__ == '__main__':
    data_store = []
    data_store.append(ScalableVolumeData(10.0, 1.0))
    data_store.append(ScalableVolumeData(5.5, 2.0))
    data_store.append(ScalableVolumeData(100.0, 0.5))
    print("--- Initial Data ---")
    for i, item in enumerate(data_store):
        print(f"Item {i}: Base={item.get_base_volume()}, Factor={item.get_scaling_factor()}, Volume={item.get_volume()}")
    print("\n--- Scaling Operation ---")
    data_store[0].scale(3.5)
    print(f"Item 0 scaled by 3.5: Volume={data_store[0].get_volume()}")
    data_store[1].scale(1.5)
    print(f"Item 1 scaled by 1.5: Volume={data_store[1].get_volume()}")
    print("\n--- Final Data ---")
    for i, item in enumerate(data_store):
        print(f"Item {i}: Base={item.get_base_volume()}, Factor={item.get_scaling_factor()}, Volume={item.get_volume()}")