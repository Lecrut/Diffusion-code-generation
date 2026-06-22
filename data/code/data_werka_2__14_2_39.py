class VolumeAnalyzer:
    def __init__(self, volumes):
        self.volumes = volumes

    def find_max_min_volumes(self):
        if not self.volumes:
            return None, None
        max_volume = float('-inf')
        min_volume = float('inf')
        for volume in self.volumes:
            if volume > max_volume:
                max_volume = volume
            if volume < min_volume:
                min_volume = volume
        return max_volume, min_volume

if __name__ == '__main__':
    sample_volumes = [15.2, 30.8, 5.4, 67.9, 22.1]
    analyzer = VolumeAnalyzer(sample_volumes)
    max_vol, min_vol = analyzer.find_max_min_volumes()
    print(f"Maximum Volume: {max_vol}, Minimum Volume: {min_vol}")