class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000.0

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(1))
    print(converter.liters_to_milliliters(0.5))
    print(converter.liters_to_milliliters(2.25))