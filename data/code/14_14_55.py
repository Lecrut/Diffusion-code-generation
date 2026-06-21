class VolumeComparator:
    UNIT = 'm^3'

    @staticmethod
    def extract_number(volume_str: str) -> float:
        number, unit = volume_str.split()
        if unit != VolumeComparator.UNIT:
            raise ValueError(f"Unsupported unit: {unit}")
        return float(number)

    def compare(self, volume1: str, volume2: str) -> bool:
        num1 = VolumeComparator.extract_number(volume1)
        num2 = VolumeComparator.extract_number(volume2)
        return num1 > num2

if __name__ == '__main__':
    comparator = VolumeComparator()
    volume_a = '4.56 m^3'
    volume_b = '2.34 m^3'
    result = comparator.compare(volume_a, volume_b)
    print(result)