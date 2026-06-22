def compare_volumes(volume1: str, volume2: str) -> bool:
    def extract_number(volume_str: str) -> float:
        unit_map = {'m^3': 1.0}
        number, unit = volume_str.split()
        multiplier = unit_map.get(unit, 1.0)
        return float(number) * multiplier

    num1 = extract_number(volume1)
    num2 = extract_number(volume2)
    return num1 > num2

if __name__ == '__main__':
    volume_a = '7.89 m^3'
    volume_b = '5.67 m^3'
    result = compare_volumes(volume_a, volume_b)
    print(result)