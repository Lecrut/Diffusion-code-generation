class VolumeAggregator:
    VOLUME_KEY = 'volume'

    @staticmethod
    def _validate_objects(objects):
        if not isinstance(objects, dict):
            raise ValueError("Input must be a dictionary.")
        for volume in objects.values():
            if not isinstance(volume, (int, float)):
                raise ValueError("All volumes must be numbers.")

    def __init__(self, objects):
        self._validate_objects(objects)
        self.objects = objects

    def calculate_total_volume(self):
        return sum(self.objects.values())

if __name__ == '__main__':
    sample_objects = {
        'cube': 27,
        'sphere': 52.36,
        'cylinder': 141.37
    }
    volume_aggregator = VolumeAggregator(sample_objects)
    print(volume_aggregator.calculate_total_volume())