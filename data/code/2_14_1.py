import math
class ScalableVolumeData:
    def __init__(self, base_volume):
        self.base_volume = base_volume
    def get_volume(self, factor):
        return self.base_volume * factor
if __name__ == '__main__':
    data_store = []
    volumes_to_store = [10.0, 5.5, 20.0]
    scaling_factors = [2.0, 1.5, 3.0]
    for base, factor in zip(volumes_to_store, scaling_factors):
        scaled_volume_object = ScalableVolumeData(base)
        data_store.append(scaled_volume_object)
    print("Data Stored (Base Volumes):")
    for item in data_store:
        print(f"Base Volume: {item.base_volume}")
    print("\nRetrieved Scaled Volumes:")
    for i, item in enumerate(data_store):
        factor = scaling_factors[i]
        result = item.get_volume(factor)
        print(f"Base {volumes_to_store[i]} scaled by {factor} = {result}")