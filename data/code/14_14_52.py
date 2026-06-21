def compare_volumes(volume1: str, volume2: str) -> bool:
    UNIT = 'm^3'
    
    def parse_volume(volume_str: str) -> float:
        if not volume_str.endswith(UNIT):
            raise ValueError(f"Unsupported unit in {volume_str}")
        number_part = volume_str[:-len(UNIT)].strip()
        return float(number_part)
    
    num1 = parse_volume(volume1)
    num2 = parse_volume(volume2)
    return num1 > num2

if __name__ == '__main__':
    volume_a = '6.78 m^3'
    volume_b = '4.56 m^3'
    result = compare_volumes(volume_a, volume_b)
    print(result)