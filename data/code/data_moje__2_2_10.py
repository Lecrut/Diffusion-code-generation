class VolumeManager:
    def __init__(self):
        self._measurements = {}

    def store(self, key, value):
        self._measurements[key] = value

    def add(self, key, value):
        if key in self._measurements:
            self._measurements[key] += value
        else:
            self._measurements[key] = value

    def get(self, key):
        if key in self._measurements:
            return self._measurements[key]
        return 0.0

    def get_all(self):
        return dict(self._measurements)

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store("tank_a", 100.5)
    manager.store("tank_b", 200.0)
    manager.add("tank_a", 50.25)
    print(manager.get("tank_a"))
    print(manager.get("tank_b"))
    print(manager.get("tank_c"))
    print(manager.get_all())