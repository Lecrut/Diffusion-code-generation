class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        if not isinstance(liters, (int, float)):
            raise TypeError("Input must be a number")
        if liters < 0:
            raise ValueError("Volume cannot be negative")
        return liters * 1000

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.liters_to_milliliters(2.5)
    print(result)