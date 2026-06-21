class VolumeComparator:
    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        self.volume1 = volume1
        self.volume2 = volume2

    def get_original_volumes(self):
        return {"volume1": self.volume1, "volume2": self.volume2}

    def calculate_ratio(self):
        larger_volume = max(self.volume1, self.volume2)
        smaller_volume = min(self.volume1, self.volume2)
        if smaller_volume == 0:
            return float('inf')
        else:
            return larger_volume / smaller_volume

    def are_volumes_equal(self):
        return self.volume1 == self.volume2

    def compare(self):
        original_volumes = self.get_original_volumes()
        ratio = self.calculate_ratio()
        are_equal = self.are_volumes_equal()
        return {
            "original_volumes": original_volumes,
            "ratio": ratio,
            "are_equal": are_equal
        }

if __name__ == '__main__':
    sample_volume1 = 75.0
    sample_volume2 = 30.0
    comparator = VolumeComparator(sample_volume1, sample_volume2)
    print(comparator.compare())