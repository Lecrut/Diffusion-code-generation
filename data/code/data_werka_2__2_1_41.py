class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("Volume must be a positive number")
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume(10.5)
    vm.add_volume(20.3)
    vm.add_volume(5.8)
    print("Total Volume:", vm.get_total_volume())
    print("Volumes:", vm.get_volumes())