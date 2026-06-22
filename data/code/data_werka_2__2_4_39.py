class VolumeScaler:
    DEFAULT_FACTOR = 1.0
    
    @staticmethod
    def validate_volumes(volumes):
        if not all(isinstance(volume, (int, float)) for volume in volumes):
            raise ValueError("All elements in volumes must be numbers.")
    
    @staticmethod
    def validate_factor(factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Factor must be a number.")
    
    def __init__(self, volumes):
        self.validate_volumes(volumes)
        self.volumes = volumes
    
    def scale(self, factor=None):
        if factor is None:
            factor = self.DEFAULT_FACTOR
        else:
            self.validate_factor(factor)
        return [float(volume) * float(factor) for volume in self.volumes]

if __name__ == '__main__':
    initial_volumes = [5.0, 10.0, 15.0]
    scaling_factor = 3.0
    scaler = VolumeScaler(initial_volumes)
    scaled_volumes = scaler.scale(scaling_factor)
    print(scaled_volumes)