class VolumeCalculator:
    @staticmethod
    def calculate_absolute_difference(volume1, volume2):
        difference = abs(volume1 - volume2)
        return f"{difference:.2f}"

if __name__ == '__main__':
    sample_volume1 = 78.901
    sample_volume2 = 75.345
    result = VolumeCalculator.calculate_absolute_difference(sample_volume1, sample_volume2)
    print(result)