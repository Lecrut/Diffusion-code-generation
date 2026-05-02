import math
class ScalableVolume:
    def __init__(self, base_volume, scale_factor):
        self.base_volume = base_volume
        self.scale_factor = scale_factor
    def get_volume(self, multiplier):
        return self.base_volume * multiplier * self.scale_factor
    def __repr__(self):
        return f"ScalableVolume(base={self.base_volume}, scale={self.scale_factor})"
class VolumeStore:
    def __init__(self):
        self.volumes = []
    def add_volume(self, base_volume, scale_factor):
        new_volume = ScalableVolume(base_volume, scale_factor)
        self.volumes.append(new_volume)
    def retrieve_volume(self, index, multiplier):
        if 0 <= index < len(self.volumes):
            return self.volumes[index].get_volume(multiplier)
        raise IndexError("Index out of bounds")
if __name__ == '__main__':
    store = VolumeStore()
    store.add_volume(10.0, 2.0)
    store.add_volume(5.5, 3.0)
    store.add_volume(100.0, 1.5)
    print("--- Stored Volumes ---")
    for i, vol in enumerate(store.volumes):
        print(f"Index {i}: {vol}")
    print("\n--- Retrieved Volumes ---")
    try:
        result1 = store.retrieve_volume(0, 5.0)
        print(f"Retrieving index 0 with multiplier 5.0: {result1}")
        result2 = store.retrieve_volume(1, 2.5)
        print(f"Retrieving index 1 with multiplier 2.5: {result2}")
        result3 = store.retrieve_volume(2, 1.0)
        print(f"Retrieving index 2 with multiplier 1.0: {result3}")
    except IndexError as e:
        print(f"Error: {e}")