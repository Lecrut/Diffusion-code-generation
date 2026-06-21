def compare_volumes(volume1: str, volume2: str) -> bool:
    def parse_volume(volume_str: str) -> float:
        number_part, _ = volume_str.split()
        return float(number_part)
    
    parsed_volume1 = parse_volume(volume1)
    parsed_volume2 = parse_volume(volume2)
    
    return parsed_volume1 > parsed_volume2

if __name__ == '__main__':
    test_volume_a = '4.56 m^3'
    test_volume_b = '1.23 m^3'
    comparison_result = compare_volumes(test_volume_a, test_volume_b)
    print(comparison_result)