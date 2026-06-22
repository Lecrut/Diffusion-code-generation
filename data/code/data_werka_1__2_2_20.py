class VolumeManager:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        self.volumes.append(volume)

    def get_volumes(self):
        return self.volumes

if __name__ == '__main__':
    manager = VolumeManager()
    manager.add_volume(10.5)
    manager.add_volume(20.3)
    manager.add_volume(30.7)
    print(manager.get_volumes())