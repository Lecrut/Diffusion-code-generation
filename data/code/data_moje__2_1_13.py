class VolumeStats:
    def __init__(self, data):
        self._data = list(data)

    def calculate_average_volume(self):
        if not self._data:
            return 0.0
        return sum(self._data) / len(self._data)

    def get_sum(self):
        return sum(self._data)

    def get_count(self):
        return len(self._data)

def calculate_average_volume(volumes):
    stats = VolumeStats(volumes)
    return stats.calculate_average_volume()

if __name__ == '__main__':
    sample_volumes = [12.5, 24.0, 18.5, 32.0, 28.0]
    stats = VolumeStats(sample_volumes)
    print(calculate_average_volume(sample_volumes))
    print(stats.get_sum())
    print(stats.get_count())