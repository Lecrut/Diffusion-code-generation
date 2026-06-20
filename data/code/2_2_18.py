class VolumeManager:
    def __init__(self):
        self._volumes = {}

    def store(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        self._volumes[key] = float(value)

    def add(self, key, increment):
        if key not in self._volumes:
            self.store(key, 0)
        if not isinstance(increment, (int, float)):
            raise TypeError("Increment must be a number")
        if increment < 0:
            raise ValueError("Increment cannot be negative")
        self._volumes[key] += float(increment)

    def get(self, key):
        if key not in self._volumes:
            return 0.0
        return self._volumes[key]

    def get_all(self):
        return dict(self._volumes)

if __name__ == '__main__':
    vm = VolumeManager()
    vm.store("tank_a", 100)
    vm.add("tank_a", 50)
    result = vm.get("tank_a")
    print(result)