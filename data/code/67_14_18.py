CONVERSION_FACTOR = 1000

class VolumeConverter:
    def __init__(self, factor):
        self.factor = factor

    def convert_to_milliliters(self, liters_list):
        if not isinstance(liters_list, list):
            raise TypeError("Input must be a list.")
        return [l * self.factor for l in liters_list]

if __name__ == '__main__':
    converter = VolumeConverter(CONVERSION_FACTOR)
    sample_volumes = [0.1, 0.5, 1.2, 5.0]
    milliliters = converter.convert_to_milliliters(sample_volumes)
    print(milliliters)