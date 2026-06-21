class VolumeAggregator:
    def __init__(self, objects):
        self.objects = objects
        self._validate_input()
    
    def _validate_input(self):
        if not isinstance(self.objects, dict):
            raise ValueError("Input must be a dictionary.")
        for volume in self.objects.values():
            if not isinstance(volume, (int, float)):
                raise ValueError("All volumes must be numbers.")
    
    def aggregate_volumes(self):
        return sum(self.objects.values())

if __name__ == '__main__':
    sample_objects = {
        'pyramid': 30.0,
        'torus': 62.83,
        'hollow_cylinder': 15.71
    }
    volume_aggregator = VolumeAggregator(sample_objects)
    print(volume_aggregator.aggregate_volumes())