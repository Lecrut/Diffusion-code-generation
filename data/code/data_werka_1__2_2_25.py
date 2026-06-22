class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        self.volumes.append(volume)

    def get_volumes(self):
        return self.volumes

    def total_volume(self):
        return sum(self.volumes)

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume(10)
    vm.add_volume(20)
    vm.add_volume(30)
    print("Volumes:", vm.get_volumes())
    print("Total Volume:", vm.total_volume())