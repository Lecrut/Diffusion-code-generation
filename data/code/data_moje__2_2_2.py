class VolumeManager:
    def __init__(self):
        self.volumes = {}

    def add_volume(self, name, volume):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")
        if volume < 0:
            raise ValueError("Volume cannot be negative")
        self.volumes[name] = float(volume)

    def store_volume(self, name, volume):
        self.add_volume(name, volume)

    def retrieve_volume(self, name):
        if name in self.volumes:
            return self.volumes[name]
        return None

    def get_all_volumes(self):
        return dict(self.volumes)

    def remove_volume(self, name):
        if name in self.volumes:
            del self.volumes[name]
            return True
        return False

if __name__ == '__main__':
    manager = VolumeManager()
    manager.add_volume("cylinder", 150.5)
    manager.add_volume("sphere", 300.0)
    manager.add_volume("cube", 125.0)
    print(manager.retrieve_volume("cylinder"))
    print(manager.retrieve_volume("sphere"))
    print(manager.retrieve_volume("nonexistent"))
    print(manager.get_all_volumes())
    manager.remove_volume("cube")
    print(manager.get_all_volumes())