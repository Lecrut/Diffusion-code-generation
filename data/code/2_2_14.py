class VolumeManager:
    def __init__(self):
        self._volumes = {}

    def store_volume(self, key, value):
        if value < 0:
            raise ValueError("Volume cannot be negative")
        self._volumes[key] = float(value)

    def add_volume(self, key, amount):
        if key not in self._volumes:
            raise KeyError(f"Volume '{key}' does not exist")
        if amount < 0:
            raise ValueError("Added amount cannot be negative")
        self._volumes[key] += float(amount)

    def get_volume(self, key):
        if key not in self._volumes:
            raise KeyError(f"Volume '{key}' does not exist")
        return self._volumes[key]

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store_volume("tank1", 100.5)
    manager.add_volume("tank1", 50.25)
    result = manager.get_volume("tank1")
    print(result)