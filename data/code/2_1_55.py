class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("Volume must be a positive number.")
        self.volumes.append(volume)

    def get_total_volume(self):
        total = sum(self.volumes)
        return total

    def get_volumes(self):
        return self.volumes.copy()

if __name__ == '__main__':
    vm = VolumeManager()
    sample_volumes = [7.1, 12.4, 9.3]
    for volume in sample_volumes:
        vm.add_volume(volume)
    
    total_volume = vm.get_total_volume()
    volumes_list = vm.get_volumes()
    
    print("Total Volume:", total_volume)
    print("Volumes List:", volumes_list)