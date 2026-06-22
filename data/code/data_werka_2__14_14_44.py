def compare_volumes(volume1: str, volume2: str) -> bool:
    def parse_volume(volume_str: str) -> float:
        parts = volume_str.split()
        if len(parts) != 2:
            raise ValueError("Invalid volume format")
        number_part, unit_part = parts
        try:
            number_value = float(number_part)
        except ValueError:
            raise ValueError("Invalid numeric part in volume")
        
        supported_units = {'m^3': 1.0}
        if unit_part not in supported_units:
            raise ValueError(f"Unsupported unit: {unit_part}")
        
        return number_value * supported_units[unit_part]
    
    parsed_volume1 = parse_volume(volume1)
    parsed_volume2 = parse_volume(volume2)
    return parsed_volume1 > parsed_volume2

if __name__ == '__main__':
    volume_a = '6.78 m^3'
    volume_b = '4.56 m^3'
    result = compare_volumes(volume_a, volume_b)
    print(result)