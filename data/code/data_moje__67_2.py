class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 2.5
    result = converter.liters_to_milliliters(sample_liters)
    print(result)