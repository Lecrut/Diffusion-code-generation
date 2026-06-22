class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000.0

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = [1.0, 2.5, 0.0, 100.0]
    for liters in sample_liters:
        result = converter.liters_to_milliliters(liters)
        print(f"{liters} liters = {result} milliliters")