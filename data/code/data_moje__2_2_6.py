class VolumeManager:
    def __init__(self):
        self.volumes = []

    def store(self, volume):
        self.volumes.append(volume)

    def add(self, volume):
        self.volumes.append(volume)

    def get_total_volume(self):
        return sum(self.volumes)

    def get_average_volume(self):
        if not self.volumes:
            return 0
        return sum(self.volumes) / len(self.volumes)

    def get_max_volume(self):
        if not self.volumes:
            return 0
        return max(self.volumes)

    def get_min_volume(self):
        if not self.volumes:
            return 0
        return min(self.volumes)

    def get_count(self):
        return len(self.volumes)

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store(10.5)
    manager.add(20.3)
    manager.store(5.2)
    total = manager.get_total_volume()
    print(total)
    average = manager.get_average_volume()
    print(average)
    maximum = manager.get_max_volume()
    print(maximum)
    minimum = manager.get_min_volume()
    print(minimum)
    count = manager.get_count()
    print(count)