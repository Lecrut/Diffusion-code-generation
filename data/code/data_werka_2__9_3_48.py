def convert_to_liters(volume, unit):
    conversion_factors = {
        'ml': 1e-3,
        'cl': 1e-2,
        'dl': 1e-1,
        'l': 1.0,
        'fl oz': 29.57352968995848,
        'cup': 0.2365882365,
        'pint': 0.473176473,
        'quart': 0.946352946,
        'gallon': 3.785411784
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit]

if __name__ == '__main__':
    sample_volumes = [
        (100, 'ml'),
        (250, 'cl'),
        (500, 'dl'),
        (1, 'l'),
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pint'),
        (1, 'quart'),
        (1, 'gallon')
    ]
    
    for volume, unit in sample_volumes:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")