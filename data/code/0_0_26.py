def convert_length(length: float, unit_type: str) -> float:
    if unit_type == 'm':
        return length
    elif unit_type == 'ft':
        return length * 0.3048
    else:
        raise ValueError(f"Unsupported unit type: {unit_type}")

if __name__ == '__main__':
    result_meters = convert_length(10, 'm')
    print(result_meters)
    
    result_feet = convert_length(10, 'ft')
    print(result_feet)