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
    
    def get_total_volume(self):
        return sum(self.objects.values())
    
    def get_individual_volumes(self):
        return self.objects

if __name__ == '__main__':
    sample_objects = {
        'pyramid': 30.0,
        'torus': 157.08,
        'hollow_cylinder': 28.27
    }
    
    volume_aggregator = VolumeAggregator(sample_objects)
    
    print("Total Volume:", volume_aggregator.get_total_volume())
    print("Individual Volumes:", volume_aggregator.get_individual_volumes())