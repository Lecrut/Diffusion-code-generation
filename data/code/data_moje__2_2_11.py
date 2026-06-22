class VolumeManager:
    def __init__(self):
        self._volumes = []

    def store(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be a number")
        if value < 0:
            raise ValueError("Volume value cannot be negative")
        self._volumes.append(float(value))

    def add(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if index < 0 or index >= len(self._volumes):
            raise IndexError("Index out of range")
        if value < 0:
            raise ValueError("Added value cannot be negative")
        self._volumes[index] += float(value)

    def get(self, index):
        if index < 0 or index >= len(self._volumes):
            raise IndexError("Index out of range")
        return self._volumes[index]

    def get_all(self):
        return list(self._volumes)

    def count(self):
        return len(self._volumes)

    def clear(self):
        self._volumes.clear()

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store(10.5)
    manager.store(20.0)
    manager.store(5.5)
    manager.add(0, 4.5)
    print(manager.get(0))
    print(manager.get(1))
    print(manager.get_all())
    print(manager.count())