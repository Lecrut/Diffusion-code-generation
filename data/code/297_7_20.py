class VolumeConverter:
    GALLONS_PER_CUBIC_METER = 264.172

    @staticmethod
    def cubic_meters_to_gallons(cubic_meters):
        return cubic_meters * VolumeConverter.GALLONS_PER_CUBIC_METER

if __name__ == '__main__':
    print(VolumeConverter.cubic_meters_to_gallons(1))
    print(VolumeConverter.cubic_meters_to_gallons(2))