class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000.0

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liter_values = [0, 1, 0.5, 2.5, 10.123]
    for liters in sample_liter_values:
        milliliters = converter.liters_to_milliliters(liters)
        print(f"{liters} liters = {milliliters} milliliters")