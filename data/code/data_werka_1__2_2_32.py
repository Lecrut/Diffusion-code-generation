class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if isinstance(volume, (int, float)) and volume > 0:
            self.volumes.append(volume)
        else:
            raise ValueError("Volume must be a positive number")

    def get_volumes(self):
        return self.volumes

    def total_volume(self):
        return sum(self.volumes)

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume(10.5)
    vm.add_volume(20.3)
    vm.add_volume(5.8)
    print("Volumes:", vm.get_volumes())
    print("Total Volume:", vm.total_volume())