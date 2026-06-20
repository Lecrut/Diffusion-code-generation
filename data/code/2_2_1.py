class VolumeManager:
    def __init__(self):
        self.volumes = {}

    def store(self, key, value):
        self.volumes[key] = value

    def add(self, key, amount):
        if key in self.volumes:
            self.volumes[key] += amount
        else:
            self.volumes[key] = amount

    def get(self, key):
        return self.volumes.get(key, 0.0)

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store('tank_a', 100.5)
    manager.add('tank_a', 50.0)
    result = manager.get('tank_a')
    print(result)