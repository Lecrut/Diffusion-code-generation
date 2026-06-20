class VolumeStorage:
    def __init__(self):
        self._data = {}

    def store(self, key, volume):
        self._data[key] = volume

    def get_base(self, key):
        if key in self._data:
            return self._data[key]
        return 0

    def get_scaled(self, key, factor):
        if key in self._data:
            return self._data[key] * factor
        return 0

    def remove(self, key):
        if key in self._data:
            del self._data[key]
            return True
        return False

    def list_keys(self):
        return list(self._data.keys())

    def clear(self):
        self._data.clear()

if __name__ == '__main__':
    vs = VolumeStorage()
    vs.store("tank_a", 100)
    vs.store("tank_b", 250.5)
    
    base_a = vs.get_base("tank_a")
    print(f"Base volume A: {base_a}")
    
    scaled_a = vs.get_scaled("tank_a", 1.5)
    print(f"Scaled volume A (1.5x): {scaled_a}")
    
    keys = vs.list_keys()
    print(f"Stored keys: {keys}")
    
    vs.remove("tank_b")
    remaining = vs.list_keys()
    print(f"Keys after removal: {remaining}")
    
    missing = vs.get_base("nonexistent")
    print(f"Missing key base: {missing}")
    
    scaled_missing = vs.get_scaled("nonexistent", 2)
    print(f"Missing key scaled: {scaled_missing}")