class VolumeManager:
    def __init__(self):
        self._volumes = {}
        self._order = []

    def store(self, key, value):
        if key not in self._volumes:
            self._order.append(key)
        self._volumes[key] = value

    def add(self, key, amount):
        if key not in self._volumes:
            self._order.append(key)
            self._volumes[key] = amount
        else:
            self._volumes[key] += amount

    def get(self, key):
        return self._volumes.get(key, 0)

    def get_all(self):
        return {key: self._volumes[key] for key in self._order}

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store("tank_a", 100.0)
    manager.store("tank_b", 250.5)
    manager.add("tank_a", 50.0)
    manager.add("tank_b", -25.5)
    print(manager.get("tank_a"))
    print(manager.get("tank_b"))
    print(manager.get_all())