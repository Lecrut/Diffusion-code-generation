class Volume:
    def __init__(self, volume_str: str):
        self.number = float(volume_str.split()[0])

    def is_greater_than(self, other_volume: 'Volume') -> bool:
        return self.number > other_volume.number

if __name__ == '__main__':
    volume_a = Volume('4.56 m^3')
    volume_b = Volume('2.34 m^3')
    result1 = volume_a.is_greater_than(volume_b)
    print(result1)

    volume_c = Volume('6.78 m^3')
    volume_d = Volume('6.78 m^3')
    result2 = volume_c.is_greater_than(volume_d)
    print(result2)

    volume_e = Volume('1.23 m^3')
    volume_f = Volume('4.56 m^3')
    result3 = volume_e.is_greater_than(volume_f)
    print(result3)