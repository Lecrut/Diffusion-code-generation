class VolumeManager:
    MIN_VOLUME = 0

    def __init__(self):
        self.volumes = []

    @staticmethod
    def validate_volume(volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number.")
        if volume <= VolumeManager.MIN_VOLUME:
            raise ValueError("Volume must be a positive number.")

    def add_volume(self, volume):
        self.validate_volume(volume)
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes.copy()

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume(12.5)
    vm.add_volume(43.7)
    vm.add_volume(8.9)
    print("Total Volume:", vm.get_total_volume())
    print("Volumes List:", vm.get_volumes())