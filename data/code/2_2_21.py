class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        self.volumes.append(volume)

    def get_volumes(self):
        return self.volumes

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume(10.5)
    vm.add_volume(20.3)
    vm.add_volume(30.7)
    print(vm.get_volumes())