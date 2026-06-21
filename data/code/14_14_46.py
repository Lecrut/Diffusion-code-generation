class VolumeComparator:
    UNIT_MULTIPLIER = {'m^3': 1.0}

    @staticmethod
    def extract_number(volume_str: str) -> float:
        number, unit = volume_str.split()
        multiplier = VolumeComparator.UNIT_MULTIPLIER.get(unit, 1.0)
        return float(number) * multiplier

    @staticmethod
    def compare_volumes(volume1: str, volume2: str) -> bool:
        num1 = VolumeComparator.extract_number(volume1)
        num2 = VolumeComparator.extract_number(volume2)
        return num1 > num2

if __name__ == '__main__':
    sample_volume1 = '4.56 m^3'
    sample_volume2 = '3.98 m^3'
    result = VolumeComparator.compare_volumes(sample_volume1, sample_volume2)
    print(result)