class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("Volume must be a positive number.")
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes.copy()

if __name__ == '__main__':
    vm = VolumeManager()
    volumes_to_add = [12.4, 34.6, 7.8]
    for volume in volumes_to_add:
        vm.add_volume(volume)
    print("Total Volume:", vm.get_total_volume())
    print("Volumes List:", vm.get_volumes())