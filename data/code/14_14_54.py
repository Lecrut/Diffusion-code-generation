def compare_volumes(volume1: str, volume2: str) -> bool:
    def parse_volume(volume_str: str) -> float:
        number_part, unit_part = volume_str.split()
        if unit_part != 'm^3':
            raise ValueError("Unsupported unit")
        return float(number_part)
    
    num1 = parse_volume(volume1)
    num2 = parse_volume(volume2)
    
    return num1 > num2

if __name__ == '__main__':
    sample_volume_a = '4.56 m^3'
    sample_volume_b = '3.21 m^3'
    result = compare_volumes(sample_volume_a, sample_volume_b)
    print(result)