class VolumeConverter:
    CUBIC_METERS_TO_CUBIC_FEET = 35.3147

    @staticmethod
    def cubic_meters_to_cubic_feet(cubic_meters):
        return int(round(cubic_meters * VolumeConverter.CUBIC_METERS_TO_CUBIC_FEET))

if __name__ == '__main__':
    sample_volume_cm = 10
    result_cf = VolumeConverter.cubic_meters_to_cubic_feet(sample_volume_cm)
    print(f"{sample_volume_cm} cubic meters is equal to {result_cf} cubic feet")