class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        if liters < 0:
            raise ValueError("Volume cannot be negative")
        return liters * 1000

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [1.0, 0.5, 2.5, 10.125]
    for value in sample_values:
        result = VolumeConverter.liters_to_milliliters(value)
        print(result)