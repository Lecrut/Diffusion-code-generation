class VolumeCalculator:
    def __init__(self, objects):
        self.objects = objects
        self._validate_input()

    def _validate_input(self):
        if not isinstance(self.objects, dict):
            raise ValueError("Input must be a dictionary.")
        for volume in self.objects.values():
            if not isinstance(volume, (int, float)):
                raise ValueError("All volumes must be numbers.")

    def calculate_total_volume(self):
        return sum(self.objects.values())

if __name__ == '__main__':
    sample_objects = {
        'cone': 12.57,
        'prism': 94.25,
        'ellipsoid': 300.0
    }
    calculator = VolumeCalculator(sample_objects)
    print(calculator.calculate_total_volume())