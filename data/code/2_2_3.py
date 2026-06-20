import math

class VolumeManager:
    def __init__(self):
        self._measurements = []
        self._lookup = {}

    def store(self, volume_id, value):
        if not isinstance(value, (int, float)) or math.isnan(value) or math.isinf(value):
            raise ValueError("Invalid volume value")
        self._measurements.append(volume_id)
        self._lookup[volume_id] = value

    def add(self, volume_id, value):
        if not isinstance(value, (int, float)) or math.isnan(value) or math.isinf(value):
            raise ValueError("Invalid volume value")
        if volume_id in self._lookup:
            self._lookup[volume_id] += value
        else:
            self._lookup[volume_id] = value
            self._measurements.append(volume_id)

    def retrieve(self, volume_id):
        if volume_id not in self._lookup:
            raise KeyError("Volume ID not found")
        return self._lookup[volume_id]

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store("tank_a", 100.5)
    manager.store("tank_b", 200.0)
    manager.add("tank_a", 50.25)
    result_a = manager.retrieve("tank_a")
    result_b = manager.retrieve("tank_b")
    print(result_a)
    print(result_b)