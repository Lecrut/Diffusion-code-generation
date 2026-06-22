class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000.0

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.liters_to_milliliters(2.5)
    print(result)