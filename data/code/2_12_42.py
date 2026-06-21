class VolumeScaler:
    FEET_PER_METER = 3.28084

    def __init__(self, conversion_factor=FEET_PER_METER):
        self.conversion_factor = conversion_factor ** 3

    def scale_volume(self, meters):
        if not isinstance(meters, (int, float)):
            raise TypeError("Volume must be a number")
        if meters < 0:
            raise ValueError("Volume cannot be negative")
        return meters * self.conversion_factor

if __name__ == '__main__':
    scaler = VolumeScaler()
    sample_values = [2.5, 8.0, 15.0, 0]
    for value in sample_values:
        try:
            result = scaler.scale_volume(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except (ValueError, TypeError) as e:
            print(e)