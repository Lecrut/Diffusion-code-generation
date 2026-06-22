class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)) or volume < 0:
            raise ValueError("Volume must be a non-negative number")
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes.copy()

if __name__ == '__main__':
    manager = VolumeManager()
    manager.add_volume(10.5)
    manager.add_volume(20.3)
    manager.add_volume(5.2)

    print("Total Volume:", manager.get_total_volume())
    print("Volumes:", manager.get_volumes())