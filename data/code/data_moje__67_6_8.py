LITERS_TO_ML_FACTOR = 1000

class VolumeConverter:
    def __init__(self, liters):
        if not isinstance(liters, (int, float)):
            raise TypeError("Liters must be a number")
        if liters < 0:
            raise ValueError("Liters cannot be negative")
        self.liters = liters

    def to_milliliters(self):
        return self.liters * LITERS_TO_ML_FACTOR

if __name__ == '__main__':
    converter = VolumeConverter(10)
    print(converter.to_milliliters())