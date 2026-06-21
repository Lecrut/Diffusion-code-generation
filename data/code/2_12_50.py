class VolumeScaler:
    M3_TO_F3_CONVERSION_FACTOR = 3.28084 ** 3
    
    def __init__(self):
        self.conversion_factor = self.M3_TO_F3_CONVERSION_FACTOR
    
    def scale(self, volume_m3):
        if volume_m3 < 0:
            raise ValueError("Volume cannot be negative")
        return volume_m3 * self.conversion_factor

if __name__ == '__main__':
    scaler = VolumeScaler()
    sample_values = [2.5, 8.0, 15.0, 0]
    for value in sample_values:
        try:
            result = scaler.scale(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except ValueError as e:
            print(e)