class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters: float) -> int:
        return int(liters * 1000)

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 2.5
    result = converter.liters_to_milliliters(sample_liters)
    print(result)
    sample_liters_2 = 0.001
    result_2 = converter.liters_to_milliliters(sample_liters_2)
    print(result_2)