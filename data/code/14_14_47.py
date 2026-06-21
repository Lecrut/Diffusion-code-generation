VOLUME_UNIT = 'm^3'

def parse_volume(volume_str: str) -> float:
    number, unit = volume_str.split()
    if unit != VOLUME_UNIT:
        raise ValueError(f"Unsupported unit: {unit}")
    return float(number)

def compare_volumes(volume1: str, volume2: str) -> bool:
    num1 = parse_volume(volume1)
    num2 = parse_volume(volume2)
    return num1 > num2

if __name__ == '__main__':
    test_volume_a = '4.56 m^3'
    test_volume_b = '1.23 m^3'
    result = compare_volumes(test_volume_a, test_volume_b)
    print(result)