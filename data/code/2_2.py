class VolumeManager:
    def __init__(self):
        self.volumes = {}

    def store_volume(self, name, value):
        if value < 0:
            raise ValueError("Volume must be non-negative")
        self.volumes[name] = value

    def add_volume(self, name, value):
        if name not in self.volumes:
            self.store_volume(name, value)
        else:
            self.volumes[name] += value

    def get_volume(self, name):
        return self.volumes.get(name, None)

    def get_all_volumes(self):
        return dict(self.volumes)

if __name__ == '__main__':
    vm = VolumeManager()
    vm.store_volume("box1", 100)
    vm.store_volume("box2", 200)
    vm.add_volume("box1", 50)
    print(vm.get_volume("box1"))
    print(vm.get_volume("box2"))
    print(vm.get_volume("nonexistent"))
    print(vm.get_all_volumes())