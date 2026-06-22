class VolumeScaler:
    FEET_PER_METER = 3.28084

    @staticmethod
    def scale_cubic_meters_to_cubic_feet(meters):
        if meters < 0:
            raise ValueError("Volume cannot be negative")
        return meters * (VolumeScaler.FEET_PER_METER ** 3)

if __name__ == '__main__':
    sample_values = [2.5, 8.0, 15.0, -3]
    for value in sample_values:
        try:
            result = VolumeScaler.scale_cubic_meters_to_cubic_feet(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except ValueError as e:
            print(e)