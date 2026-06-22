class VolumeScaler:
    METERS_TO_FEET = 3.28084

    def __init__(self):
        self.cubic_feet_per_cubic_meter = self.METERS_TO_FEET ** 3

    def scale(self, cubic_meters):
        if cubic_meters < 0:
            raise ValueError("Volume cannot be negative")
        return cubic_meters * self.cubic_feet_per_cubic_meter

if __name__ == '__main__':
    scaler = VolumeScaler()
    sample_values = [2.5, 15.0, 30.0, 0]
    for value in sample_values:
        try:
            result = scaler.scale(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except ValueError as e:
            print(e)