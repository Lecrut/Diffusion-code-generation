class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number.")
        if volume <= 0:
            raise ValueError("Volume must be a positive number.")
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes.copy()

if __name__ == '__main__':
    vm = VolumeManager()
    try:
        vm.add_volume(15.2)
        vm.add_volume(30.8)
        vm.add_volume(7.4)
        print("Total Volume:", vm.get_total_volume())
        print("Volumes List:", vm.get_volumes())
    except ValueError as e:
        print(e)