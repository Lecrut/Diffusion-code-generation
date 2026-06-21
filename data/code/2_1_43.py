class VolumeManager:
    MIN_VOLUME = 0.1

    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number.")
        if volume < VolumeManager.MIN_VOLUME:
            raise ValueError(f"Volume must be at least {VolumeManager.MIN_VOLUME}.")
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes.copy()

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume(12.0)
    vm.add_volume(18.5)
    vm.add_volume(7.3)
    print("Total Volume:", vm.get_total_volume())
    print("Volumes List:", vm.get_volumes())