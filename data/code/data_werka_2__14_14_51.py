def compare_volumes(volume1: str, volume2: str) -> bool:

    def parse_volume(volume_str: str):
        try:
            value = float(volume_str.split()[0])
            return value
        except (ValueError, IndexError):
            raise ValueError('Invalid volume format')
    vol1 = parse_volume(volume1)
    vol2 = parse_volume(volume2)
    return vol1 > vol2
if __name__ == '__main__':
    sample_volume1 = '3.50 m^3'
    sample_volume2 = '2.75 m^3'
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)