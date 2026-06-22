class VolumeConverter:
    CUBIC_METERS_TO_CUBIC_FEET = 35.3147

    @staticmethod
    def cubic_meters_to_cubic_feet(cubic_meters):
        return int(cubic_meters * VolumeConverter.CUBIC_METERS_TO_CUBIC_FEET)

if __name__ == '__main__':
    sample_cubic_meters = 10
    result_cubic_feet = VolumeConverter.cubic_meters_to_cubic_feet(sample_cubic_meters)
    print(f"{sample_cubic_meters} cubic meters is equal to {result_cubic_feet} cubic feet")