def compare_volumes(volume1: str, volume2: str) -> bool:
    def parse_volume(volume_str: str) -> float:
        number_part, unit_part = volume_str.split()
        if unit_part != 'm^3':
            raise ValueError(f"Unsupported unit: {unit_part}")
        return float(number_part)

    volume1_number = parse_volume(volume1)
    volume2_number = parse_volume(volume2)
    return volume1_number > volume2_number

if __name__ == '__main__':
    test_volume_a = '6.78 m^3'
    test_volume_b = '4.56 m^3'
    comparison_result = compare_volumes(test_volume_a, test_volume_b)
    print(comparison_result)