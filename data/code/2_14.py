import math
class ScalableVolumeStore:
    def __init__(self):
        self.base_volumes = {}
    def store_volume(self, name, volume):
        if name not in self.base_volumes:
            self.base_volumes[name] = volume
    def get_volume(self, name):
        if name in self.base_volumes:
            return self.base_volumes[name]
        return None
    def scale_volume(self, name, factor):
        if name in self.base_volumes:
            new_volume = self.base_volumes[name] * factor
            self.base_volumes[name] = new_volume
            return new_volume
        return None
    def get_scaled_volume(self, name, factor):
        if name in self.base_volumes:
            return self.base_volumes[name] * factor
        return None
if __name__ == '__main__':
    store = ScalableVolumeStore()
    store.store_volume("A", 10.0)
    store.store_volume("B", 5.5)
    print(f"Base volume A: {store.get_volume('A')}")
    print(f"Base volume B: {store.get_volume('B')}")
    factor1 = 2.0
    scaled_a = store.scale_volume("A", factor1)
    print(f"Scaled volume A by {factor1}: {scaled_a}")
    print(f"Current volume A: {store.get_volume('A')}")
    factor2 = 1.5
    scaled_b = store.get_scaled_volume("B", factor2)
    print(f"Scaled volume B by {factor2}: {scaled_b}")
    print(f"Current volume B: {store.get_volume('B')}")
    factor3 = 3.0
    scaled_a_again = store.get_scaled_volume("A", factor3)
    print(f"Scaled volume A by {factor3}: {scaled_a_again}")
    print(f"Current volume A: {store.get_volume('A')}")