class VolumeManager:
    def __init__(self):
        self._volumes = []

    def store(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be a number")
        self._volumes.append(float(value))

    def add(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be a number")
        new_volume = float(value)
        if self._volumes:
            self._volumes[-1] += new_volume
        else:
            self._volumes.append(new_volume)

    def get_all(self):
        return list(self._volumes)

    def get_sum(self):
        total = 0
        for v in self._volumes:
            total += v
        return total

    def get_latest(self):
        if not self._volumes:
            return None
        return self._volumes[-1]

    def get_count(self):
        return len(self._volumes)

    def clear(self):
        self._volumes = []

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store(10)
    manager.store(20)
    manager.add(5)
    manager.add(15)
    manager.store(30)
    result_sum = manager.get_sum()
    result_latest = manager.get_latest()
    result_all = manager.get_all()
    result_count = manager.get_count()
    print(result_sum)
    print(result_latest)
    print(result_all)
    print(result_count)
    manager.clear()
    print(manager.get_count())
    print(manager.get_latest())