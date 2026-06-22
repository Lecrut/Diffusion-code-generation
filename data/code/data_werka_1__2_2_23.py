class VolumeManager:

    def __init__(self):
        self.volumes = {}

    def store_volume(self, key, value):
        self.volumes[key] = value

    def add_volume(self, key, increment):
        if key in self.volumes:
            self.volumes[key] += increment
        else:
            self.volumes[key] = increment

    def retrieve_volume(self, key):
        return self.volumes.get(key, None)
if __name__ == '__main__':
    vm = VolumeManager()
    vm.store_volume('room1', 50.5)
    vm.add_volume('room1', 20.3)
    vm.store_volume('room2', 75.0)
    print(vm.retrieve_volume('room1'))
    print(vm.retrieve_volume('room2'))
    print(vm.retrieve_volume('room3'))