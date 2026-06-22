class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if isinstance(volume, (int, float)) and volume > 0:
            self.volumes.append(volume)
        else:
            raise ValueError("Volume must be a positive number")

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes

if __name__ == '__main__':
    vm = VolumeManager()
    sample_volumes = [10.5, 20.3, 5.8]
    for volume in sample_volumes:
        vm.add_volume(volume)
    
    print("Total Volume:", vm.get_total_volume())
    print("Volumes List:", vm.get_volumes())