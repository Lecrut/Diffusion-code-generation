class VolumeManager:
    def __init__(self):
        self.volumes = {}

    def store_volume(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be a number")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        self.volumes[key] = float(value)

    def add_volume(self, key, increment):
        if not isinstance(increment, (int, float)):
            raise TypeError("Increment must be a number")
        if key not in self.volumes:
            raise KeyError(f"Key '{key}' does not exist")
        new_value = self.volumes[key] + float(increment)
        if new_value < 0:
            raise ValueError("Resulting volume cannot be negative")
        self.volumes[key] = new_value

    def retrieve_volume(self, key):
        if key not in self.volumes:
            raise KeyError(f"Key '{key}' does not exist")
        return self.volumes[key]

    def get_all_volumes(self):
        return dict(self.volumes)

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store_volume('tank_a', 100.5)
    manager.store_volume('tank_b', 250.0)
    manager.add_volume('tank_a', 10.0)
    result_a = manager.retrieve_volume('tank_a')
    result_b = manager.retrieve_volume('tank_b')
    all_volumes = manager.get_all_volumes()
    print(result_a)
    print(result_b)
    print(all_volumes)