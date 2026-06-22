class VolumeConverter:
    GALLONS_TO_LITERS_FACTOR = 3.78541
    LITERS_TO_GALLONS_FACTOR = 0.264172

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * VolumeConverter.GALLONS_TO_LITERS_FACTOR

    @staticmethod
    def liters_to_gallons(liters):
        return liters * VolumeConverter.LITERS_TO_GALLONS_FACTOR

if __name__ == '__main__':
    print(VolumeConverter.gallons_to_liters(1))
    print(VolumeConverter.liters_to_gallons(1))