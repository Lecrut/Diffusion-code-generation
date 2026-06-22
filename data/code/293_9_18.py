def convert_storage_units(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        'bytes': 1,
        'kilobytes': 1024,
        'megabytes': 1024 ** 2,
        'gigabytes': 1024 ** 3,
        'terabytes': 1024 ** 4,
        'petabytes': 1024 ** 5,
        'exabytes': 1024 ** 6
    }
    
    from_factor = conversion_factors.get(from_unit.lower(), None)
    to_factor = conversion_factors.get(to_unit.lower(), None)
    
    if from_factor is None or to_factor is None:
        raise ValueError("Invalid unit provided")
    
    return (value / from_factor) * to_factor

if __name__ == '__main__':
    print(convert_storage_units(1, 'gigabytes', 'terabytes'))
    print(convert_storage_units(512, 'kilobytes', 'bytes'))
    print(convert_storage_units(10, 'exabytes', 'petabytes'))