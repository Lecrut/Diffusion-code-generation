class VolumeManager:

    def __init__(self):
        self.volumes = []

    def add_volume(self, volume):
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError('Volume must be a positive number.')
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_volumes(self):
        return self.volumes.copy()
if __name__ == '__main__':
    volume_manager = VolumeManager()
    try:
        volume_manager.add_volume(12.7)
        volume_manager.add_volume(45.3)
        volume_manager.add_volume(8.9)
    except ValueError as e:
        print(e)
    total_volume = volume_manager.get_total_volume()
    print('Total Volume:', total_volume)
    volumes_list = volume_manager.get_volumes()
    print('Volumes List:', volumes_list)