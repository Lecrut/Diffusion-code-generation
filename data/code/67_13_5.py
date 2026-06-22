class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return float(liters) * 1000.0

if __name__ == '__main__':
    result = VolumeConverter.liters_to_milliliters(1.5)
    print(result)