class VolumeComparator:

    def __init__(self, volume1: str, volume2: str):
        self.volume1 = volume1
        self.volume2 = volume2

    def extract_number(self, volume_str: str) -> float:
        number, unit = volume_str.split()
        if unit != 'm^3':
            raise ValueError('Unsupported unit')
        return float(number)

    def compare(self) -> bool:
        num1 = self.extract_number(self.volume1)
        num2 = self.extract_number(self.volume2)
        return num1 > num2
if __name__ == '__main__':
    volume_a = '4.56 m^3'
    volume_b = '1.23 m^3'
    comparator = VolumeComparator(volume_a, volume_b)
    result = comparator.compare()
    print(result)
    volume_c = '6.78 m^3'
    volume_d = '6.78 m^3'
    comparator2 = VolumeComparator(volume_c, volume_d)
    result2 = comparator2.compare()
    print(result2)
    volume_e = '2.34 m^3'
    volume_f = '5.67 m^3'
    comparator3 = VolumeComparator(volume_e, volume_f)
    result3 = comparator3.compare()
    print(result3)