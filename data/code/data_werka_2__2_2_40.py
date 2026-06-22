class VolumeAggregator:
    def __init__(self, object_volumes):
        self.object_volumes = object_volumes
        self._validate_input()

    def _validate_input(self):
        if not isinstance(self.object_volumes, dict):
            raise ValueError("Input must be a dictionary.")
        for volume in self.object_volumes.values():
            if not isinstance(volume, (int, float)):
                raise ValueError("All volumes must be numbers.")

    def aggregate_volumes(self):
        return sum(self.object_volumes.values())

if __name__ == '__main__':
    sample_objects = {
        'parallelepiped': 50.4,
        'hollow_cylinder': 23.7,
        'spherical_cap': 18.09
    }
    volume_aggregator = VolumeAggregator(sample_objects)
    total_volume = volume_aggregator.aggregate_volumes()
    print(total_volume)