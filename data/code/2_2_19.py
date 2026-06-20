class VolumeManager:
    def __init__(self):
        self._volumes = {}

    def store(self, key, volume):
        if volume < 0:
            raise ValueError("Volume cannot be negative")
        self._volumes[key] = volume

    def add(self, key, volume):
        if volume < 0:
            raise ValueError("Added volume cannot be negative")
        if key in self._volumes:
            self._volumes[key] += volume
        else:
            self._volumes[key] = volume

    def retrieve(self, key):
        if key not in self._volumes:
            raise KeyError(f"Key '{key}' not found")
        return self._volumes[key]

if __name__ == '__main__':
    vm = VolumeManager()
    vm.store("cylinder1", 100.5)
    vm.add("cylinder1", 50.0)
    vm.store("sphere1", 200.0)
    result1 = vm.retrieve("cylinder1")
    result2 = vm.retrieve("sphere1")
    print(result1)
    print(result2)