class VolumeManager:
    def __init__(self):
        self._volumes = []

    def store(self, volume):
        if not isinstance(volume, (int, float)):
            raise TypeError("Volume must be a number")
        self._volumes.append(float(volume))

    def add(self, *volumes):
        for volume in volumes:
            if not isinstance(volume, (int, float)):
                raise TypeError("Volume must be a number")
            self._volumes.append(float(volume))

    def retrieve(self, index=None):
        if index is None:
            return list(self._volumes)
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(self._volumes):
            raise IndexError("Index out of range")
        return self._volumes[index]

    def total(self):
        return sum(self._volumes)

    def count(self):
        return len(self._volumes)

    def clear(self):
        self._volumes = []

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store(10.5)
    manager.add(20.0, 5.5, 30.0)
    manager.store(15.0)
    print(manager.retrieve(0))
    print(manager.retrieve(2))
    print(manager.total())
    print(manager.count())
    print(manager.retrieve())